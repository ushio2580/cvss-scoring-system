from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.user import User, UserRole
from app.models.database_info import DatabaseQuery
from app.services.database_manager import DatabaseManagerService
from app import db
import json

database_bp = Blueprint('database', __name__)

def admin_required(f):
    """Decorator para requerir rol de administrador"""
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        current_user_id = get_jwt_identity()
        current_user = User.query.get(current_user_id)
        
        if not current_user or current_user.role != UserRole.ADMIN:
            return jsonify({'error': 'Admin access required'}), 403
        return f(*args, **kwargs)
    return decorated_function

@database_bp.route('/info', methods=['GET'])
@jwt_required()
@admin_required
def get_database_info():
    """Obtener información general de la base de datos"""
    try:
        info = DatabaseManagerService.get_database_info()
        return jsonify(info), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@database_bp.route('/tables/<table_name>/structure', methods=['GET'])
@jwt_required()
@admin_required
def get_table_structure(table_name):
    """Obtener estructura de una tabla específica"""
    try:
        structure = DatabaseManagerService.get_table_structure(table_name)
        return jsonify(structure), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@database_bp.route('/tables/<table_name>/data', methods=['GET'])
@jwt_required()
@admin_required
def get_table_data(table_name):
    """Obtener datos de una tabla con paginación"""
    try:
        limit = request.args.get('limit', 100, type=int)
        offset = request.args.get('offset', 0, type=int)
        
        data = DatabaseManagerService.get_table_data(table_name, limit, offset)
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@database_bp.route('/tables/<table_name>/count', methods=['GET'])
@jwt_required()
@admin_required
def get_table_count(table_name):
    """Obtener el número total de filas en una tabla"""
    try:
        count = DatabaseManagerService.get_table_count(table_name)
        return jsonify(count), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@database_bp.route('/execute', methods=['POST'])
@jwt_required()
@admin_required
def execute_query():
    """Ejecutar una consulta SQL personalizada"""
    try:
        current_user_id = get_jwt_identity()
        current_user = User.query.get(current_user_id)
        
        data = request.get_json()
        query_text = data.get('query')
        query_type = data.get('type', 'SELECT')
        
        if not query_text:
            return jsonify({'error': 'Query text is required'}), 400
        
        # Ejecutar la consulta
        success, result, execution_time = DatabaseManagerService.execute_query(query_text, query_type)
        
        # Registrar la consulta en el historial
        db_query = DatabaseQuery(
            user_id=current_user_id,
            username=current_user.name,
            query_type=query_type.upper(),
            query_text=query_text,
            execution_time=execution_time,
            success=success,
            error_message=result.get('error') if not success else None,
            ip_address=request.remote_addr
        )
        db.session.add(db_query)
        db.session.commit()
        
        if success:
            return jsonify({
                'success': True,
                'result': result,
                'execution_time': execution_time,
                'query_id': db_query.id
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': result.get('error'),
                'execution_time': execution_time,
                'query_id': db_query.id
            }), 400
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@database_bp.route('/suggestions', methods=['GET'])
@jwt_required()
@admin_required
def get_query_suggestions():
    """Obtener sugerencias de consultas comunes"""
    try:
        suggestions = DatabaseManagerService.get_query_suggestions()
        return jsonify({'suggestions': suggestions}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@database_bp.route('/queries', methods=['GET'])
@jwt_required()
@admin_required
def get_query_history():
    """Obtener historial de consultas ejecutadas"""
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 50, type=int)
        
        queries = DatabaseQuery.query.order_by(DatabaseQuery.timestamp.desc()).paginate(
            page=page, per_page=per_page, error_out=False
        )
        
        return jsonify({
            'queries': [query.to_dict() for query in queries.items],
            'pagination': {
                'page': queries.page,
                'per_page': queries.per_page,
                'total': queries.total,
                'pages': queries.pages,
                'has_next': queries.has_next,
                'has_prev': queries.has_prev
            }
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@database_bp.route('/queries/<int:query_id>', methods=['GET'])
@jwt_required()
@admin_required
def get_query_details(query_id):
    """Obtener detalles de una consulta específica"""
    try:
        query = DatabaseQuery.query.get_or_404(query_id)
        return jsonify(query.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@database_bp.route('/export/<table_name>', methods=['GET'])
@jwt_required()
@admin_required
def export_table_data(table_name):
    """Exportar datos de una tabla a CSV"""
    try:
        import csv
        from io import StringIO
        
        # Obtener datos de la tabla
        data = DatabaseManagerService.get_table_data(table_name, limit=10000, offset=0)
        
        if 'error' in data:
            return jsonify(data), 400
        
        # Crear CSV
        output = StringIO()
        writer = csv.writer(output)
        
        # Escribir headers
        if data.get('columns'):
            writer.writerow(data['columns'])
        
        # Escribir datos
        for row in data.get('data', []):
            writer.writerow([row.get(col, '') for col in data['columns']])
        
        output.seek(0)
        
        from flask import Response
        return Response(
            output.getvalue(),
            mimetype='text/csv',
            headers={'Content-Disposition': f'attachment; filename={table_name}_export.csv'}
        )
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
