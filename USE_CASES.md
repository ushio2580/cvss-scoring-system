# 📋 **CASOS DE USO - CVSS SCORING SYSTEM**

## 📋 **INFORMACIÓN GENERAL**
- **Proyecto:** CVSS Scoring System
- **Versión:** 1.0
- **Fecha:** Septiembre 2025
- **Metodología:** SCRUM
- **Actores:** Usuario, Administrador, Sistema

---

## 🎭 **ACTORES DEL SISTEMA**

### **👤 Usuario (Usuario Final)**
- **Descripción:** Persona que utiliza el sistema para evaluar vulnerabilidades
- **Responsabilidades:**
  - Crear y gestionar vulnerabilidades
  - Analizar documentos
  - Calcular scores CVSS
  - Seguir el estado de vulnerabilidades

### **👨‍💼 Administrador**
- **Descripción:** Persona responsable de la administración del sistema
- **Responsabilidades:**
  - Gestionar usuarios
  - Configurar el sistema
  - Monitorear el rendimiento
  - Resolver problemas técnicos

### **🤖 Sistema**
- **Descripción:** Componentes automáticos del sistema
- **Responsabilidades:**
  - Procesar análisis de documentos
  - Calcular scores CVSS
  - Gestionar autenticación
  - Almacenar datos

---

## 📊 **DIAGRAMA DE CASOS DE USO PRINCIPAL**

```
                    CVSS SCORING SYSTEM
                           |
        ┌──────────────────┼──────────────────┐
        |                  |                  |
    👤 USUARIO         👨‍💼 ADMIN         🤖 SISTEMA
        |                  |                  |
        |                  |                  |
    ┌───▼───┐          ┌───▼───┐          ┌───▼───┐
    |       |          |       |          |       |
    | UC-01 |          | UC-08 |          | UC-15 |
    | Login |          | Admin |          | Auto  |
    |       |          | Mgmt  |          | Calc  |
    └───┬───┘          └───┬───┘          └───┬───┘
        |                  |                  |
    ┌───▼───┐          ┌───▼───┐          ┌───▼───┐
    |       |          |       |          |       |
    | UC-02 |          | UC-09 |          | UC-16 |
    | Manage|          | System|          | File  |
    | Vulns |          | Config|          | Proc  |
    └───┬───┘          └───┬───┘          └───┬───┘
        |                  |                  |
    ┌───▼───┐          ┌───▼───┐          ┌───▼───┐
    |       |          |       |          |       |
    | UC-03 |          | UC-10 |          | UC-17 |
    | Calc  |          | Monitor|         | Data  |
    | CVSS  |          | System |         | Store |
    └───┬───┘          └───┬───┘          └───┬───┘
        |                  |                  |
    ┌───▼───┐          ┌───▼───┐              |
    |       |          |       |              |
    | UC-04 |          | UC-11 |              |
    | Track |          | Reports|              |
    | Status|          |       |              |
    └───┬───┘          └───┬───┘              |
        |                  |                  |
    ┌───▼───┐          ┌───▼───┐              |
    |       |          |       |              |
    | UC-05 |          | UC-12 |              |
    | Analyze|         | Backup|              |
    | Docs  |          | Data  |              |
    └───┬───┘          └───┬───┘              |
        |                  |                  |
    ┌───▼───┐          ┌───▼───┐              |
    |       |          |       |              |
    | UC-06 |          | UC-13 |              |
    | View   |         | Audit |              |
    | History|         | Logs  |              |
    └───┬───┘          └───┬───┘              |
        |                  |                  |
    ┌───▼───┐              |                  |
    |       |              |                  |
    | UC-07 |              |                  |
    | Convert|             |                  |
    | to Vuln|             |                  |
    └───────┘              |                  |
                           |                  |
                    ┌──────▼──────┐           |
                    |             |           |
                    | UC-14       |           |
                    | Security    |           |
                    | Management  |           |
                    └─────────────┘           |
```

---

## 📝 **CASOS DE USO DETALLADOS**

### **UC-01: Iniciar Sesión**
- **ID:** UC-01
- **Actor Principal:** Usuario
- **Actor Secundario:** Sistema
- **Descripción:** El usuario inicia sesión en el sistema usando credenciales válidas
- **Precondiciones:** Usuario registrado en el sistema
- **Flujo Principal:**
  1. Usuario accede a la página de login
  2. Usuario ingresa email y contraseña
  3. Sistema valida credenciales
  4. Sistema genera token JWT
  5. Sistema redirige al dashboard
  6. Usuario accede al sistema
- **Flujos Alternativos:**
  - **3a:** Credenciales inválidas
    - 3a.1: Sistema muestra mensaje de error
    - 3a.2: Usuario permanece en página de login
- **Postcondiciones:** Usuario autenticado en el sistema
- **Prioridad:** Alta
- **Frecuencia:** Alta

### **UC-02: Gestionar Vulnerabilidades**
- **ID:** UC-02
- **Actor Principal:** Usuario
- **Actor Secundario:** Sistema
- **Descripción:** El usuario crea, edita, visualiza y elimina vulnerabilidades
- **Precondiciones:** Usuario autenticado
- **Flujo Principal:**
  1. Usuario navega a la sección de vulnerabilidades
  2. Usuario selecciona acción (crear/editar/eliminar)
  3. Sistema presenta formulario apropiado
  4. Usuario completa información
  5. Sistema valida datos
  6. Sistema guarda cambios
  7. Sistema actualiza lista de vulnerabilidades
- **Flujos Alternativos:**
  - **5a:** Datos inválidos
    - 5a.1: Sistema muestra errores de validación
    - 5a.2: Usuario corrige errores
    - 5a.3: Continúa en paso 5
- **Postcondiciones:** Vulnerabilidades actualizadas en el sistema
- **Prioridad:** Alta
- **Frecuencia:** Alta

### **UC-03: Calcular Score CVSS**
- **ID:** UC-03
- **Actor Principal:** Usuario
- **Actor Secundario:** Sistema
- **Descripción:** El usuario calcula el score CVSS de una vulnerabilidad
- **Precondiciones:** Usuario autenticado
- **Flujo Principal:**
  1. Usuario accede a la calculadora CVSS
  2. Usuario selecciona métricas base
  3. Usuario selecciona métricas temporales (opcional)
  4. Usuario selecciona métricas ambientales (opcional)
  5. Sistema calcula score CVSS
  6. Sistema muestra resultado y severidad
  7. Usuario puede guardar resultado
- **Flujos Alternativos:**
  - **5a:** Error en cálculo
    - 5a.1: Sistema muestra mensaje de error
    - 5a.2: Usuario revisa métricas seleccionadas
- **Postcondiciones:** Score CVSS calculado y mostrado
- **Prioridad:** Alta
- **Frecuencia:** Media

### **UC-04: Seguir Estado de Vulnerabilidades**
- **ID:** UC-04
- **Actor Principal:** Usuario
- **Actor Secundario:** Sistema
- **Descripción:** El usuario monitorea y actualiza el estado de vulnerabilidades
- **Precondiciones:** Vulnerabilidades existentes en el sistema
- **Flujo Principal:**
  1. Usuario visualiza lista de vulnerabilidades
  2. Usuario selecciona vulnerabilidad
  3. Usuario actualiza estado (Nuevo/En Progreso/Resuelto/Cerrado)
  4. Sistema valida transición de estado
  5. Sistema actualiza estado
  6. Sistema envía notificaciones si es necesario
- **Flujos Alternativos:**
  - **4a:** Transición de estado inválida
    - 4a.1: Sistema muestra mensaje de error
    - 4a.2: Usuario selecciona estado válido
- **Postcondiciones:** Estado de vulnerabilidad actualizado
- **Prioridad:** Media
- **Frecuencia:** Media

### **UC-05: Analizar Documentos**
- **ID:** UC-05
- **Actor Principal:** Usuario
- **Actor Secundario:** Sistema
- **Descripción:** El usuario analiza documentos PDF/Word para detectar vulnerabilidades
- **Precondiciones:** Usuario autenticado, documento válido
- **Flujo Principal:**
  1. Usuario navega a Document Analyzer
  2. Usuario sube archivo PDF o Word
  3. Sistema valida tipo y tamaño de archivo
  4. Sistema extrae texto del documento
  5. Sistema analiza texto buscando patrones de vulnerabilidades
  6. Sistema calcula scores CVSS para vulnerabilidades detectadas
  7. Sistema genera recomendaciones
  8. Sistema muestra resultados del análisis
- **Flujos Alternativos:**
  - **3a:** Archivo inválido
    - 3a.1: Sistema muestra mensaje de error
    - 3a.2: Usuario selecciona archivo válido
  - **4a:** Error en extracción de texto
    - 4a.1: Sistema muestra mensaje de error
    - 4a.2: Usuario intenta con otro documento
- **Postcondiciones:** Análisis de documento completado y guardado
- **Prioridad:** Alta
- **Frecuencia:** Media

### **UC-06: Ver Historial de Análisis**
- **ID:** UC-06
- **Actor Principal:** Usuario
- **Actor Secundario:** Sistema
- **Descripción:** El usuario visualiza el historial de análisis de documentos
- **Precondiciones:** Análisis de documentos realizados
- **Flujo Principal:**
  1. Usuario navega a Analysis History
  2. Sistema muestra lista de análisis realizados
  3. Usuario puede filtrar por fecha, archivo, o estado
  4. Usuario selecciona análisis específico
  5. Sistema muestra detalles completos del análisis
  6. Usuario puede descargar reporte si es necesario
- **Flujos Alternativos:**
  - **2a:** No hay análisis disponibles
    - 2a.1: Sistema muestra mensaje informativo
    - 2a.2: Usuario puede realizar nuevo análisis
- **Postcondiciones:** Historial de análisis visualizado
- **Prioridad:** Media
- **Frecuencia:** Baja

### **UC-07: Convertir Análisis a Vulnerabilidad**
- **ID:** UC-07
- **Actor Principal:** Usuario
- **Actor Secundario:** Sistema
- **Descripción:** El usuario convierte un análisis de documento en una vulnerabilidad del dashboard
- **Precondiciones:** Análisis de documento completado
- **Flujo Principal:**
  1. Usuario visualiza resultados de análisis
  2. Usuario hace clic en "Add to Dashboard"
  3. Sistema valida datos del análisis
  4. Sistema crea nueva vulnerabilidad
  5. Sistema asigna vulnerabilidad al usuario
  6. Sistema marca análisis como convertido
  7. Sistema muestra mensaje de confirmación
- **Flujos Alternativos:**
  - **3a:** Datos de análisis inválidos
    - 3a.1: Sistema muestra mensaje de error
    - 3a.2: Usuario revisa análisis
- **Postcondiciones:** Vulnerabilidad creada en el dashboard
- **Prioridad:** Alta
- **Frecuencia:** Media

---

## 👨‍💼 **CASOS DE USO - ADMINISTRADOR**

### **UC-08: Gestionar Usuarios**
- **ID:** UC-08
- **Actor Principal:** Administrador
- **Actor Secundario:** Sistema
- **Descripción:** El administrador gestiona usuarios del sistema
- **Precondiciones:** Administrador autenticado
- **Flujo Principal:**
  1. Administrador accede a gestión de usuarios
  2. Administrador puede crear, editar, o eliminar usuarios
  3. Administrador asigna roles y permisos
  4. Sistema valida cambios
  5. Sistema actualiza base de datos de usuarios
- **Postcondiciones:** Usuarios gestionados correctamente
- **Prioridad:** Media
- **Frecuencia:** Baja

### **UC-09: Configurar Sistema**
- **ID:** UC-09
- **Actor Principal:** Administrador
- **Actor Secundario:** Sistema
- **Descripción:** El administrador configura parámetros del sistema
- **Precondiciones:** Administrador autenticado
- **Flujo Principal:**
  1. Administrador accede a configuración del sistema
  2. Administrador modifica parámetros (límites de archivo, timeouts, etc.)
  3. Sistema valida configuración
  4. Sistema aplica cambios
  5. Sistema reinicia servicios si es necesario
- **Postcondiciones:** Sistema configurado según parámetros
- **Prioridad:** Media
- **Frecuencia:** Baja

### **UC-10: Monitorear Sistema**
- **ID:** UC-10
- **Actor Principal:** Administrador
- **Actor Secundario:** Sistema
- **Descripción:** El administrador monitorea el rendimiento del sistema
- **Precondiciones:** Administrador autenticado
- **Flujo Principal:**
  1. Administrador accede a panel de monitoreo
  2. Sistema muestra métricas de rendimiento
  3. Administrador puede configurar alertas
  4. Sistema notifica problemas si los hay
- **Postcondiciones:** Sistema monitoreado
- **Prioridad:** Media
- **Frecuencia:** Media

---

## 🤖 **CASOS DE USO - SISTEMA**

### **UC-15: Cálculo Automático CVSS**
- **ID:** UC-15
- **Actor Principal:** Sistema
- **Actor Secundario:** Usuario
- **Descripción:** El sistema calcula automáticamente scores CVSS
- **Precondiciones:** Métricas CVSS proporcionadas
- **Flujo Principal:**
  1. Sistema recibe métricas CVSS
  2. Sistema valida métricas
  3. Sistema aplica algoritmo CVSS v3.1
  4. Sistema calcula score base
  5. Sistema calcula score temporal (si aplica)
  6. Sistema calcula score ambiental (si aplica)
  7. Sistema determina severidad
  8. Sistema retorna resultados
- **Postcondiciones:** Score CVSS calculado
- **Prioridad:** Alta
- **Frecuencia:** Alta

### **UC-16: Procesamiento de Archivos**
- **ID:** UC-16
- **Actor Principal:** Sistema
- **Actor Secundario:** Usuario
- **Descripción:** El sistema procesa archivos PDF/Word para extraer texto
- **Precondiciones:** Archivo válido subido
- **Flujo Principal:**
  1. Sistema recibe archivo
  2. Sistema valida tipo y tamaño
  3. Sistema extrae texto usando bibliotecas apropiadas
  4. Sistema limpia y formatea texto
  5. Sistema retorna texto extraído
- **Flujos Alternativos:**
  - **2a:** Archivo inválido
    - 2a.1: Sistema retorna error
  - **3a:** Error en extracción
    - 3a.1: Sistema retorna error con detalles
- **Postcondiciones:** Texto extraído del archivo
- **Prioridad:** Alta
- **Frecuencia:** Media

### **UC-17: Almacenamiento de Datos**
- **ID:** UC-17
- **Actor Principal:** Sistema
- **Actor Secundario:** Usuario
- **Descripción:** El sistema almacena y recupera datos del sistema
- **Precondiciones:** Datos válidos para almacenar
- **Flujo Principal:**
  1. Sistema recibe datos para almacenar
  2. Sistema valida estructura de datos
  3. Sistema ejecuta operación de base de datos
  4. Sistema confirma transacción
  5. Sistema retorna confirmación
- **Flujos Alternativos:**
  - **2a:** Datos inválidos
    - 2a.1: Sistema retorna error de validación
  - **3a:** Error de base de datos
    - 3a.1: Sistema hace rollback
    - 3a.2: Sistema retorna error
- **Postcondiciones:** Datos almacenados correctamente
- **Prioridad:** Alta
- **Frecuencia:** Alta

---

## 📊 **DIAGRAMA DE FLUJO - CASO DE USO PRINCIPAL**

### **Flujo de Análisis de Documento:**

```
    Usuario
       |
       ▼
   [Subir Archivo]
       |
       ▼
   [Validar Archivo]
       |
       ▼
   [Extraer Texto]
       |
       ▼
   [Analizar Vulnerabilidades]
       |
       ▼
   [Calcular CVSS]
       |
       ▼
   [Generar Recomendaciones]
       |
       ▼
   [Mostrar Resultados]
       |
       ▼
   [¿Convertir a Vulnerabilidad?]
       |
    ┌───▼───┐
    |  SÍ   |
    └───┬───┘
        |
        ▼
   [Crear Vulnerabilidad]
       |
       ▼
   [Actualizar Dashboard]
       |
       ▼
   [Mostrar Confirmación]
```

---

## 🔗 **RELACIONES ENTRE CASOS DE USO**

### **Inclusión (Include):**
- **UC-02** incluye **UC-15** (Gestionar Vulnerabilidades incluye Cálculo CVSS)
- **UC-05** incluye **UC-16** (Analizar Documentos incluye Procesamiento de Archivos)
- **UC-07** incluye **UC-02** (Convertir Análisis incluye Gestionar Vulnerabilidades)

### **Extensión (Extend):**
- **UC-06** extiende **UC-05** (Ver Historial extiende Analizar Documentos)
- **UC-04** extiende **UC-02** (Seguir Estado extiende Gestionar Vulnerabilidades)

### **Generalización:**
- **UC-01** es generalización de login de usuario y administrador
- **UC-17** es generalización de todas las operaciones de almacenamiento

---

## 📈 **MÉTRICAS DE CASOS DE USO**

### **Estadísticas:**
- **Total de Casos de Uso:** 17
- **Casos de Usuario:** 7
- **Casos de Administrador:** 3
- **Casos de Sistema:** 3
- **Casos de Seguridad:** 4

### **Prioridades:**
- **Alta:** 8 casos
- **Media:** 7 casos
- **Baja:** 2 casos

### **Frecuencias:**
- **Alta:** 4 casos
- **Media:** 10 casos
- **Baja:** 3 casos

---

## 🎯 **REQUISITOS NO FUNCIONALES**

### **Rendimiento:**
- **Tiempo de respuesta:** < 3 segundos para operaciones básicas
- **Procesamiento de archivos:** < 30 segundos para archivos de 10MB
- **Cálculo CVSS:** < 1 segundo

### **Disponibilidad:**
- **Uptime:** 99.5%
- **Tiempo de recuperación:** < 5 minutos

### **Seguridad:**
- **Autenticación:** JWT con expiración de 24 horas
- **Autorización:** Control de acceso basado en roles
- **Encriptación:** HTTPS para todas las comunicaciones

### **Usabilidad:**
- **Interfaz responsive:** Compatible con móviles y tablets
- **Accesibilidad:** Cumple estándares WCAG 2.1
- **Idioma:** Interfaz en inglés

---

**✅ Total de Casos de Uso: 17**
**📅 Fecha de Creación: Septiembre 2025**
**👥 Responsable: Equipo de Desarrollo**
