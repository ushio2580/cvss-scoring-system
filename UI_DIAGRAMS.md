# 🎨 **DIAGRAMAS DE INTERFAZ DE USUARIO - CVSS SCORING SYSTEM**

## 📋 **INFORMACIÓN GENERAL**
- **Proyecto:** CVSS Scoring System
- **Versión:** 1.0
- **Fecha:** Septiembre 2025
- **Framework:** React + TypeScript
- **Styling:** Tailwind CSS + shadcn/ui
- **Responsive:** Mobile-first design

---

## 🎯 **PRINCIPIOS DE DISEÑO**

### **Design System:**
- **Colores:** Paleta profesional con azules y grises
- **Tipografía:** Inter font family
- **Espaciado:** Sistema de 8px (0.5rem, 1rem, 1.5rem, 2rem, etc.)
- **Componentes:** shadcn/ui como base
- **Iconos:** Lucide React
- **Animaciones:** Framer Motion

### **Paleta de Colores:**
```css
/* Primary Colors */
--primary: #3b82f6;      /* Blue-500 */
--primary-dark: #2563eb; /* Blue-600 */
--primary-light: #60a5fa; /* Blue-400 */

/* Secondary Colors */
--secondary: #64748b;    /* Slate-500 */
--secondary-dark: #475569; /* Slate-600 */
--secondary-light: #94a3b8; /* Slate-400 */

/* Status Colors */
--success: #10b981;      /* Emerald-500 */
--warning: #f59e0b;      /* Amber-500 */
--error: #ef4444;        /* Red-500 */
--info: #06b6d4;         /* Cyan-500 */

/* Neutral Colors */
--background: #ffffff;   /* White */
--surface: #f8fafc;      /* Slate-50 */
--border: #e2e8f0;       /* Slate-200 */
--text: #1e293b;         /* Slate-800 */
--text-muted: #64748b;   /* Slate-500 */
```

---

## 🏠 **DASHBOARD PRINCIPAL**

### **Layout del Dashboard:**
```
┌─────────────────────────────────────────────────────────────────┐
│ HEADER                                                          │
│ ┌─────────────┐ ┌─────────────────────────────────────────────┐ │
│ │    LOGO     │ │                    NAVIGATION                │ │
│ │   CVSS      │ │ Dashboard | Vulns | Calc | Docs | History   │ │
│ └─────────────┘ └─────────────────────────────────────────────┘ │
├─────────────────────────────────────────────────────────────────┤
│ SIDEBAR                    │ MAIN CONTENT                       │
│ ┌─────────────────────────┐ │ ┌─────────────────────────────────┐ │
│ │ 🏠 Dashboard            │ │ │ Welcome Back, User!             │ │
│ │ 🛡️ Vulnerabilities     │ │ │                                 │ │
│ │ 🧮 CVSS Calculator      │ │ │ ┌─────────┐ ┌─────────┐        │ │
│ │ 📄 Document Analyzer    │ │ │ │  Total  │ │  High   │        │ │
│ │ 📚 Analysis History     │ │ │ │ Vulns   │ │ Severity│        │ │
│ │ 👤 Profile              │ │ │ │   45    │ │    12   │        │ │
│ │ 🚪 Logout               │ │ │ └─────────┘ └─────────┘        │ │
│ └─────────────────────────┘ │ │                                 │ │
│                            │ │ ┌─────────┐ ┌─────────┐        │ │
│                            │ │ │ Recent  │ │ Recent  │        │ │
│                            │ │ │ Vulns   │ │ Docs    │        │ │
│                            │ │ │   5     │ │    3    │        │ │
│                            │ │ └─────────┘ └─────────┘        │ │
│                            │ │                                 │ │
│                            │ │ ┌─────────────────────────────┐ │ │
│                            │ │ │     QUICK ACTIONS           │ │ │
│                            │ │ │                             │ │ │
│                            │ │ │ [Add Vulnerability]         │ │ │
│                            │ │ │ [Analyze Document]          │ │ │
│                            │ │ │ [Calculate CVSS]            │ │ │
│                            │ │ └─────────────────────────────┘ │ │
│                            │ └─────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

### **Componentes del Dashboard:**

#### **1. Header Component:**
```jsx
<header className="bg-white border-b border-gray-200 px-6 py-4">
  <div className="flex items-center justify-between">
    <div className="flex items-center space-x-4">
      <Shield className="h-8 w-8 text-blue-600" />
      <h1 className="text-2xl font-bold text-gray-900">CVSS Scoring System</h1>
    </div>
    <nav className="hidden md:flex space-x-8">
      <NavLink to="/dashboard">Dashboard</NavLink>
      <NavLink to="/vulnerabilities">Vulnerabilities</NavLink>
      <NavLink to="/cvss-calculator">Calculator</NavLink>
      <NavLink to="/document-analyzer">Analyzer</NavLink>
    </nav>
    <UserMenu />
  </div>
</header>
```

#### **2. Sidebar Component:**
```jsx
<aside className="w-64 bg-gray-50 border-r border-gray-200 min-h-screen">
  <nav className="p-4 space-y-2">
    <SidebarItem icon={Home} label="Dashboard" to="/dashboard" />
    <SidebarItem icon={Shield} label="Vulnerabilities" to="/vulnerabilities" />
    <SidebarItem icon={Calculator} label="CVSS Calculator" to="/cvss-calculator" />
    <SidebarItem icon={FileText} label="Document Analyzer" to="/document-analyzer" />
    <SidebarItem icon={History} label="Analysis History" to="/document-analysis-history" />
    <SidebarItem icon={User} label="Profile" to="/profile" />
    <SidebarItem icon={LogOut} label="Logout" onClick={handleLogout} />
  </nav>
</aside>
```

#### **3. Stats Cards:**
```jsx
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
  <StatCard
    title="Total Vulnerabilities"
    value="45"
    icon={Shield}
    trend="+12%"
    color="blue"
  />
  <StatCard
    title="High Severity"
    value="12"
    icon={AlertTriangle}
    trend="+3%"
    color="red"
  />
  <StatCard
    title="Documents Analyzed"
    value="23"
    icon={FileText}
    trend="+8%"
    color="green"
  />
  <StatCard
    title="Avg CVSS Score"
    value="7.2"
    icon={TrendingUp}
    trend="-0.5"
    color="orange"
  />
</div>
```

---

## 🛡️ **GESTIÓN DE VULNERABILIDADES**

### **Layout de Vulnerabilidades:**
```
┌─────────────────────────────────────────────────────────────────┐
│ HEADER                                                          │
│ ┌─────────────┐ ┌─────────────────────────────────────────────┐ │
│ │    LOGO     │ │                    NAVIGATION                │ │
│ │   CVSS      │ │ Dashboard | Vulns | Calc | Docs | History   │ │
│ └─────────────┘ └─────────────────────────────────────────────┘ │
├─────────────────────────────────────────────────────────────────┤
│ SIDEBAR                    │ MAIN CONTENT                       │
│ ┌─────────────────────────┐ │ ┌─────────────────────────────────┐ │
│ │ 🏠 Dashboard            │ │ │ VULNERABILITIES                 │ │
│ │ 🛡️ Vulnerabilities     │ │ │                                 │ │
│ │ 🧮 CVSS Calculator      │ │ │ ┌─────────────────────────────┐ │ │
│ │ 📄 Document Analyzer    │ │ │ │ [Add New] [Filter] [Search] │ │ │
│ │ 📚 Analysis History     │ │ │ └─────────────────────────────┘ │ │
│ │ 👤 Profile              │ │ │                                 │ │
│ │ 🚪 Logout               │ │ │ ┌─────────────────────────────┐ │ │
│ └─────────────────────────┘ │ │ │ VULNERABILITY LIST           │ │ │
│                            │ │ │                               │ │ │
│                            │ │ │ ┌─────────────────────────┐   │ │ │
│                            │ │ │ │ SQL Injection           │   │ │ │
│                            │ │ │ │ CVSS: 9.8 (Critical)    │   │ │ │
│                            │ │ │ │ Status: New             │   │ │ │
│                            │ │ │ │ [View] [Edit] [Delete]  │   │ │ │
│                            │ │ │ └─────────────────────────┘   │ │ │
│                            │ │ │                               │ │ │
│                            │ │ │ ┌─────────────────────────┐   │ │ │
│                            │ │ │ │ XSS Vulnerability       │   │ │ │
│                            │ │ │ │ CVSS: 6.1 (Medium)      │   │ │ │
│                            │ │ │ │ Status: In Progress     │   │ │ │
│                            │ │ │ │ [View] [Edit] [Delete]  │   │ │ │
│                            │ │ │ └─────────────────────────┘   │ │ │
│                            │ │ └─────────────────────────────┘ │ │
│                            │ └─────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

### **Vulnerability Card Component:**
```jsx
<div className="bg-white rounded-lg border border-gray-200 p-6 shadow-sm hover:shadow-md transition-shadow">
  <div className="flex items-start justify-between">
    <div className="flex-1">
      <h3 className="text-lg font-semibold text-gray-900 mb-2">
        {vulnerability.title}
      </h3>
      <p className="text-gray-600 text-sm mb-3 line-clamp-2">
        {vulnerability.description}
      </p>
      <div className="flex items-center space-x-4">
        <Badge variant={getSeverityVariant(vulnerability.severity)}>
          CVSS: {vulnerability.cvss_score} ({vulnerability.severity})
        </Badge>
        <Badge variant="outline">
          {vulnerability.status}
        </Badge>
      </div>
    </div>
    <div className="flex items-center space-x-2">
      <Button variant="ghost" size="sm">
        <Eye className="h-4 w-4" />
      </Button>
      <Button variant="ghost" size="sm">
        <Edit className="h-4 w-4" />
      </Button>
      <Button variant="ghost" size="sm">
        <Trash2 className="h-4 w-4" />
      </Button>
    </div>
  </div>
</div>
```

### **Create/Edit Vulnerability Modal:**
```jsx
<Dialog>
  <DialogContent className="max-w-2xl">
    <DialogHeader>
      <DialogTitle>Create New Vulnerability</DialogTitle>
    </DialogHeader>
    <form onSubmit={handleSubmit} className="space-y-6">
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div>
          <Label htmlFor="title">Title *</Label>
          <Input
            id="title"
            value={formData.title}
            onChange={(e) => setFormData({...formData, title: e.target.value})}
            placeholder="Enter vulnerability title"
          />
        </div>
        <div>
          <Label htmlFor="severity">Severity</Label>
          <Select value={formData.severity} onValueChange={(value) => setFormData({...formData, severity: value})}>
            <SelectTrigger>
              <SelectValue placeholder="Select severity" />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="low">Low</SelectItem>
              <SelectItem value="medium">Medium</SelectItem>
              <SelectItem value="high">High</SelectItem>
              <SelectItem value="critical">Critical</SelectItem>
            </SelectContent>
          </Select>
        </div>
      </div>
      
      <div>
        <Label htmlFor="description">Description *</Label>
        <Textarea
          id="description"
          value={formData.description}
          onChange={(e) => setFormData({...formData, description: e.target.value})}
          placeholder="Enter vulnerability description"
          rows={4}
        />
      </div>
      
      <div>
        <Label htmlFor="cvss_vector">CVSS Vector</Label>
        <Input
          id="cvss_vector"
          value={formData.cvss_vector}
          onChange={(e) => setFormData({...formData, cvss_vector: e.target.value})}
          placeholder="CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H"
        />
      </div>
      
      <DialogFooter>
        <Button type="button" variant="outline" onClick={onClose}>
          Cancel
        </Button>
        <Button type="submit">
          {isEditing ? 'Update' : 'Create'} Vulnerability
        </Button>
      </DialogFooter>
    </form>
  </DialogContent>
</Dialog>
```

---

## 🧮 **CALCULADORA CVSS**

### **Layout de Calculadora CVSS:**
```
┌─────────────────────────────────────────────────────────────────┐
│ HEADER                                                          │
│ ┌─────────────┐ ┌─────────────────────────────────────────────┐ │
│ │    LOGO     │ │                    NAVIGATION                │ │
│ │   CVSS      │ │ Dashboard | Vulns | Calc | Docs | History   │ │
│ └─────────────┘ └─────────────────────────────────────────────┘ │
├─────────────────────────────────────────────────────────────────┤
│ SIDEBAR                    │ MAIN CONTENT                       │
│ ┌─────────────────────────┐ │ ┌─────────────────────────────────┐ │
│ │ 🏠 Dashboard            │ │ │ CVSS CALCULATOR                 │ │
│ │ 🛡️ Vulnerabilities     │ │ │                                 │ │
│ │ 🧮 CVSS Calculator      │ │ │ ┌─────────────────────────────┐ │ │
│ │ 📄 Document Analyzer    │ │ │ │     BASE METRICS             │ │ │
│ │ 📚 Analysis History     │ │ │ │                             │ │ │
│ │ 👤 Profile              │ │ │ │ Attack Vector: [Network ▼]  │ │ │
│ │ 🚪 Logout               │ │ │ │ Attack Complexity: [Low ▼]  │ │ │
│ └─────────────────────────┘ │ │ │ Privileges Required: [None▼]│ │ │
│                            │ │ │ User Interaction: [None ▼]   │ │ │
│                            │ │ │ Scope: [Unchanged ▼]         │ │ │
│                            │ │ │ Confidentiality: [High ▼]    │ │ │
│                            │ │ │ Integrity: [High ▼]          │ │ │
│                            │ │ │ Availability: [High ▼]       │ │ │
│                            │ │ └─────────────────────────────┘ │ │
│                            │ │                                 │ │
│                            │ │ ┌─────────────────────────────┐ │ │
│                            │ │ │   TEMPORAL METRICS          │ │ │
│                            │ │ │                             │ │ │
│                            │ │ │ Exploit Code Maturity: [▼]  │ │ │
│                            │ │ │ Remediation Level: [▼]      │ │ │
│                            │ │ │ Report Confidence: [▼]      │ │ │
│                            │ │ └─────────────────────────────┘ │ │
│                            │ │                                 │ │
│                            │ │ ┌─────────────────────────────┐ │ │
│                            │ │ │   ENVIRONMENTAL METRICS     │ │ │
│                            │ │ │                             │ │ │
│                            │ │ │ Confidentiality: [▼]        │ │ │
│                            │ │ │ Integrity: [▼]              │ │ │
│                            │ │ │ Availability: [▼]           │ │ │
│                            │ │ │ Modified Base: [▼]          │ │ │
│                            │ │ └─────────────────────────────┘ │ │
│                            │ │                                 │ │
│                            │ │ ┌─────────────────────────────┐ │ │
│                            │ │ │        RESULTS              │ │ │
│                            │ │ │                             │ │ │
│                            │ │ │ Base Score: 9.8             │ │ │
│                            │ │ │ Temporal Score: 9.1         │ │ │
│                            │ │ │ Environmental Score: 8.7    │ │ │
│                            │ │ │ Severity: Critical          │ │ │
│                            │ │ │ Vector: CVSS:3.1/AV:N/...   │ │ │
│                            │ │ └─────────────────────────────┘ │ │
│                            │ │                                 │ │
│                            │ │ ┌─────────────────────────────┐ │ │
│                            │ │ │        ACTIONS              │ │ │
│                            │ │ │                             │ │ │
│                            │ │ │ [Calculate] [Save as Vuln]  │ │ │
│                            │ │ │ [Reset] [Copy Vector]       │ │ │
│                            │ │ └─────────────────────────────┘ │ │
│                            │ └─────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

### **CVSS Metric Selector Component:**
```jsx
<div className="space-y-4">
  <div>
    <Label htmlFor="attack-vector">Attack Vector</Label>
    <Select value={metrics.attackVector} onValueChange={(value) => updateMetric('attackVector', value)}>
      <SelectTrigger>
        <SelectValue placeholder="Select attack vector" />
      </SelectTrigger>
      <SelectContent>
        <SelectItem value="N">Network (N)</SelectItem>
        <SelectItem value="A">Adjacent (A)</SelectItem>
        <SelectItem value="L">Local (L)</SelectItem>
        <SelectItem value="P">Physical (P)</SelectItem>
      </SelectContent>
    </Select>
  </div>
  
  <div>
    <Label htmlFor="attack-complexity">Attack Complexity</Label>
    <Select value={metrics.attackComplexity} onValueChange={(value) => updateMetric('attackComplexity', value)}>
      <SelectTrigger>
        <SelectValue placeholder="Select attack complexity" />
      </SelectTrigger>
      <SelectContent>
        <SelectItem value="L">Low (L)</SelectItem>
        <SelectItem value="H">High (H)</SelectItem>
      </SelectContent>
    </Select>
  </div>
</div>
```

### **Results Display Component:**
```jsx
<div className="bg-gray-50 rounded-lg p-6 space-y-4">
  <h3 className="text-lg font-semibold">CVSS Results</h3>
  
  <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
    <div className="text-center">
      <div className="text-2xl font-bold text-blue-600">{results.baseScore}</div>
      <div className="text-sm text-gray-600">Base Score</div>
    </div>
    <div className="text-center">
      <div className="text-2xl font-bold text-green-600">{results.temporalScore}</div>
      <div className="text-sm text-gray-600">Temporal Score</div>
    </div>
    <div className="text-center">
      <div className="text-2xl font-bold text-orange-600">{results.environmentalScore}</div>
      <div className="text-sm text-gray-600">Environmental Score</div>
    </div>
  </div>
  
  <div className="text-center">
    <Badge variant={getSeverityVariant(results.severity)} className="text-lg px-4 py-2">
      {results.severity}
    </Badge>
  </div>
  
  <div className="bg-white rounded border p-4">
    <Label className="text-sm font-medium">CVSS Vector String</Label>
    <div className="mt-2 p-2 bg-gray-100 rounded font-mono text-sm break-all">
      {results.vectorString}
    </div>
  </div>
</div>
```

---

## 📄 **ANALIZADOR DE DOCUMENTOS**

### **Layout de Document Analyzer:**
```
┌─────────────────────────────────────────────────────────────────┐
│ HEADER                                                          │
│ ┌─────────────┐ ┌─────────────────────────────────────────────┐ │
│ │    LOGO     │ │                    NAVIGATION                │ │
│ │   CVSS      │ │ Dashboard | Vulns | Calc | Docs | History   │ │
│ └─────────────┘ └─────────────────────────────────────────────┘ │
├─────────────────────────────────────────────────────────────────┤
│ SIDEBAR                    │ MAIN CONTENT                       │
│ ┌─────────────────────────┐ │ ┌─────────────────────────────────┐ │
│ │ 🏠 Dashboard            │ │ │ DOCUMENT ANALYZER               │ │
│ │ 🛡️ Vulnerabilities     │ │ │                                 │ │
│ │ 🧮 CVSS Calculator      │ │ │ ┌─────────────────────────────┐ │ │
│ │ 📄 Document Analyzer    │ │ │ │     UPLOAD AREA              │ │ │
│ │ 📚 Analysis History     │ │ │ │                             │ │ │
│ │ 👤 Profile              │ │ │ │ ┌─────────────────────────┐ │ │ │
│ │ 🚪 Logout               │ │ │ │ │                         │ │ │ │
│ └─────────────────────────┘ │ │ │ │    DRAG & DROP ZONE     │ │ │ │
│                            │ │ │ │                         │ │ │ │
│                            │ │ │ │    📄 Drop files here   │ │ │ │
│                            │ │ │ │    or click to browse   │ │ │ │
│                            │ │ │ │                         │ │ │ │
│                            │ │ │ │    [Choose File]        │ │ │ │
│                            │ │ │ └─────────────────────────┘ │ │ │
│                            │ │ └─────────────────────────────┘ │ │
│                            │ │                                 │ │
│                            │ │ ┌─────────────────────────────┐ │ │
│                            │ │ │   SUPPORTED FORMATS         │ │ │
│                            │ │ │                             │ │ │
│                            │ │ │ • PDF (.pdf) - Max 10MB     │ │ │
│                            │ │ │ • Word (.docx) - Max 10MB   │ │ │
│                            │ │ │ • Text extraction only      │ │ │
│                            │ │ └─────────────────────────────┘ │ │
│                            │ │                                 │ │
│                            │ │ ┌─────────────────────────────┐ │ │
│                            │ │ │        ACTIONS              │ │ │
│                            │ │ │                             │ │ │
│                            │ │ │ [Analyze Document]          │ │ │
│                            │ │ │ [Back to Dashboard]         │ │ │
│                            │ │ └─────────────────────────────┘ │ │
│                            │ └─────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

### **File Upload Component:**
```jsx
<div className="border-2 border-dashed border-gray-300 rounded-lg p-8 text-center hover:border-gray-400 transition-colors">
  <div className="space-y-4">
    <div className="mx-auto w-12 h-12 text-gray-400">
      <Upload className="w-full h-full" />
    </div>
    <div>
      <h3 className="text-lg font-medium text-gray-900">Upload Document</h3>
      <p className="text-gray-600">Drop your file here or click to browse</p>
    </div>
    <div>
      <Button variant="outline" onClick={() => fileInputRef.current?.click()}>
        Choose File
      </Button>
      <input
        ref={fileInputRef}
        type="file"
        accept=".pdf,.docx"
        onChange={handleFileSelect}
        className="hidden"
      />
    </div>
    {selectedFile && (
      <div className="bg-green-50 border border-green-200 rounded-lg p-4">
        <div className="flex items-center space-x-2">
          <FileText className="h-5 w-5 text-green-600" />
          <span className="text-green-800 font-medium">{selectedFile.name}</span>
          <span className="text-green-600 text-sm">({formatFileSize(selectedFile.size)})</span>
        </div>
      </div>
    )}
  </div>
</div>
```

### **Analysis Results Component:**
```jsx
<div className="space-y-6">
  {/* File Information */}
  <div className="bg-white rounded-lg border p-6">
    <h3 className="text-lg font-semibold mb-4">File Information</h3>
    <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
      <div>
        <Label className="text-sm font-medium text-gray-600">Filename</Label>
        <p className="text-gray-900">{analysis.filename}</p>
      </div>
      <div>
        <Label className="text-sm font-medium text-gray-600">Size</Label>
        <p className="text-gray-900">{formatFileSize(analysis.fileSize)}</p>
      </div>
      <div>
        <Label className="text-sm font-medium text-gray-600">Type</Label>
        <p className="text-gray-900">{analysis.fileType}</p>
      </div>
    </div>
  </div>

  {/* Vulnerabilities Detected */}
  <div className="bg-white rounded-lg border p-6">
    <h3 className="text-lg font-semibold mb-4">Vulnerabilities Detected</h3>
    <div className="space-y-3">
      {analysis.vulnerabilityTypes?.map((vuln, index) => (
        <div key={index} className="flex items-center justify-between p-3 bg-red-50 border border-red-200 rounded-lg">
          <div className="flex items-center space-x-3">
            <AlertTriangle className="h-5 w-5 text-red-600" />
            <span className="font-medium text-red-900">{vuln}</span>
          </div>
          <Badge variant="destructive">High Risk</Badge>
        </div>
      ))}
    </div>
  </div>

  {/* CVSS Score */}
  <div className="bg-white rounded-lg border p-6">
    <h3 className="text-lg font-semibold mb-4">CVSS Assessment</h3>
    <div className="text-center">
      <div className="text-4xl font-bold text-red-600 mb-2">{analysis.cvssScore}</div>
      <Badge variant="destructive" className="text-lg px-4 py-2">{analysis.severity}</Badge>
    </div>
  </div>

  {/* Recommendations */}
  <div className="bg-white rounded-lg border p-6">
    <h3 className="text-lg font-semibold mb-4">Recommendations</h3>
    <ul className="space-y-2">
      {analysis.recommendations?.map((rec, index) => (
        <li key={index} className="flex items-start space-x-2">
          <CheckCircle className="h-5 w-5 text-green-600 mt-0.5" />
          <span className="text-gray-700">{rec}</span>
        </li>
      ))}
    </ul>
  </div>

  {/* Actions */}
  <div className="flex justify-center space-x-4">
    <Button onClick={handleConvertToVulnerability} disabled={isConverting}>
      {isConverting ? 'Converting...' : 'Add to Dashboard'}
    </Button>
    <Button variant="outline" onClick={() => navigate('/document-analysis-history')}>
      View History
    </Button>
  </div>
</div>
```

---

## 📚 **HISTORIAL DE ANÁLISIS**

### **Layout de Analysis History:**
```
┌─────────────────────────────────────────────────────────────────┐
│ HEADER                                                          │
│ ┌─────────────┐ ┌─────────────────────────────────────────────┐ │
│ │    LOGO     │ │                    NAVIGATION                │ │
│ │   CVSS      │ │ Dashboard | Vulns | Calc | Docs | History   │ │
│ └─────────────┘ └─────────────────────────────────────────────┘ │
├─────────────────────────────────────────────────────────────────┤
│ SIDEBAR                    │ MAIN CONTENT                       │
│ ┌─────────────────────────┐ │ ┌─────────────────────────────────┐ │
│ │ 🏠 Dashboard            │ │ │ ANALYSIS HISTORY                │ │
│ │ 🛡️ Vulnerabilities     │ │ │                                 │ │
│ │ 🧮 CVSS Calculator      │ │ │ ┌─────────────────────────────┐ │ │
│ │ 📄 Document Analyzer    │ │ │ │ [Back to Dash] [New Analysis]│ │ │
│ │ 📚 Analysis History     │ │ │ │ [Filter] [Sort] [Search]    │ │ │
│ │ 👤 Profile              │ │ │ └─────────────────────────────┘ │ │
│ │ 🚪 Logout               │ │ │                                 │ │
│ └─────────────────────────┘ │ │ ┌─────────────────────────────┐ │ │
│                            │ │ │     ANALYSIS LIST            │ │ │
│                            │ │ │                               │ │ │
│                            │ │ │ ┌─────────────────────────┐   │ │ │
│                            │ │ │ │ security_report.pdf     │   │ │ │
│                            │ │ │ │ CVSS: 8.5 (High)        │   │ │ │
│                            │ │ │ │ 3 vulnerabilities found │   │ │ │
│                            │ │ │ │ 2025-09-12 10:30 AM     │   │ │ │
│                            │ │ │ │ [View] [Convert] [Delete]│   │ │ │
│                            │ │ │ └─────────────────────────┘   │ │ │
│                            │ │ │                               │ │ │
│                            │ │ │ ┌─────────────────────────┐   │ │ │
│                            │ │ │ │ audit_results.docx      │   │ │ │
│                            │ │ │ │ CVSS: 6.1 (Medium)      │   │ │ │
│                            │ │ │ │ 2 vulnerabilities found │   │ │ │
│                            │ │ │ │ 2025-09-11 14:20 PM     │   │ │ │
│                            │ │ │ │ [View] [Convert] [Delete]│   │ │ │
│                            │ │ │ └─────────────────────────┘   │ │ │
│                            │ │ └─────────────────────────────┘ │ │
│                            │ └─────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

### **Analysis History Card Component:**
```jsx
<div className="bg-white rounded-lg border border-gray-200 p-6 hover:shadow-md transition-shadow">
  <div className="flex items-start justify-between">
    <div className="flex-1">
      <div className="flex items-center space-x-3 mb-2">
        <FileText className="h-5 w-5 text-gray-400" />
        <h3 className="text-lg font-semibold text-gray-900">{analysis.filename}</h3>
      </div>
      
      <div className="flex items-center space-x-4 mb-3">
        <Badge variant={getSeverityVariant(analysis.severity)}>
          CVSS: {analysis.cvssScore} ({analysis.severity})
        </Badge>
        <span className="text-sm text-gray-600">
          {analysis.vulnerabilityTypes?.length || 0} vulnerabilities found
        </span>
      </div>
      
      <div className="text-sm text-gray-500">
        {formatDate(analysis.createdAt)}
      </div>
    </div>
    
    <div className="flex items-center space-x-2">
      <Button variant="ghost" size="sm" onClick={() => viewDetails(analysis.id)}>
        <Eye className="h-4 w-4" />
      </Button>
      <Button variant="ghost" size="sm" onClick={() => convertToVulnerability(analysis.id)}>
        <Plus className="h-4 w-4" />
      </Button>
      <Button variant="ghost" size="sm" onClick={() => deleteAnalysis(analysis.id)}>
        <Trash2 className="h-4 w-4" />
      </Button>
    </div>
  </div>
</div>
```

---

## 📱 **DISEÑO RESPONSIVE**

### **Breakpoints:**
```css
/* Mobile First Approach */
/* sm: 640px */
/* md: 768px */
/* lg: 1024px */
/* xl: 1280px */
/* 2xl: 1536px */
```

### **Mobile Layout (< 768px):**
```
┌─────────────────────────────────────────┐
│ HEADER: ☰ Menu | Logo | User Menu      │
├─────────────────────────────────────────┤
│ MAIN CONTENT                            │
│                                         │
│ ┌─────────────────────────────────────┐ │
│ │           PAGE CONTENT              │ │
│ │                                     │ │
│ │ • Stacked components                │ │
│ │ • Full width cards                  │ │
│ │ • Touch-friendly buttons            │ │
│ │ • Simplified navigation             │ │
│ └─────────────────────────────────────┘ │
└─────────────────────────────────────────┘
```

### **Tablet Layout (768px - 1024px):**
```
┌─────────────────────────────────────────┐
│ HEADER: Logo | ☰ Menu | User Menu      │
├─────────────────────────────────────────┤
│ MAIN CONTENT                            │
│                                         │
│ ┌─────────────────────────────────────┐ │
│ │           PAGE CONTENT              │ │
│ │                                     │ │
│ │ • 2-column grid for cards           │ │
│ │ • Collapsible sidebar               │ │
│ │ • Medium-sized components           │ │
│ └─────────────────────────────────────┘ │
└─────────────────────────────────────────┘
```

### **Desktop Layout (> 1024px):**
```
┌─────────────────────────────────────────┐
│ HEADER: Logo | Navigation | User Menu   │
├─────────────────────────────────────────┤
│ SIDEBAR │ MAIN CONTENT                  │
│         │                               │
│ • Nav   │ • 3-4 column grids            │
│ • Menu  │ • Full sidebar visible        │
│ • Items │ • Large components            │
│         │ • Hover effects               │
└─────────────────────────────────────────┘
```

---

## 🎨 **COMPONENTES REUTILIZABLES**

### **Button Component:**
```jsx
const Button = ({ variant = "default", size = "default", children, ...props }) => {
  const baseClasses = "inline-flex items-center justify-center rounded-md font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:opacity-50 disabled:pointer-events-none ring-offset-background";
  
  const variants = {
    default: "bg-primary text-primary-foreground hover:bg-primary/90",
    destructive: "bg-destructive text-destructive-foreground hover:bg-destructive/90",
    outline: "border border-input hover:bg-accent hover:text-accent-foreground",
    secondary: "bg-secondary text-secondary-foreground hover:bg-secondary/80",
    ghost: "hover:bg-accent hover:text-accent-foreground",
    link: "underline-offset-4 hover:underline text-primary"
  };
  
  const sizes = {
    default: "h-10 py-2 px-4",
    sm: "h-9 px-3 rounded-md",
    lg: "h-11 px-8 rounded-md",
    icon: "h-10 w-10"
  };
  
  return (
    <button
      className={`${baseClasses} ${variants[variant]} ${sizes[size]}`}
      {...props}
    >
      {children}
    </button>
  );
};
```

### **Card Component:**
```jsx
const Card = ({ className, ...props }) => (
  <div
    className={`rounded-lg border bg-card text-card-foreground shadow-sm ${className}`}
    {...props}
  />
);

const CardHeader = ({ className, ...props }) => (
  <div className={`flex flex-col space-y-1.5 p-6 ${className}`} {...props} />
);

const CardTitle = ({ className, ...props }) => (
  <h3 className={`text-2xl font-semibold leading-none tracking-tight ${className}`} {...props} />
);

const CardDescription = ({ className, ...props }) => (
  <p className={`text-sm text-muted-foreground ${className}`} {...props} />
);

const CardContent = ({ className, ...props }) => (
  <div className={`p-6 pt-0 ${className}`} {...props} />
);

const CardFooter = ({ className, ...props }) => (
  <div className={`flex items-center p-6 pt-0 ${className}`} {...props} />
);
```

### **Badge Component:**
```jsx
const Badge = ({ variant = "default", className, ...props }) => {
  const variants = {
    default: "bg-primary hover:bg-primary/80 text-primary-foreground",
    secondary: "bg-secondary hover:bg-secondary/80 text-secondary-foreground",
    destructive: "bg-destructive hover:bg-destructive/80 text-destructive-foreground",
    outline: "text-foreground border border-input"
  };
  
  return (
    <div
      className={`inline-flex items-center rounded-full border px-2.5 py-0.5 text-xs font-semibold transition-colors focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 ${variants[variant]} ${className}`}
      {...props}
    />
  );
};
```

---

## 🎯 **ACCESIBILIDAD**

### **ARIA Labels:**
```jsx
<button
  aria-label="Delete vulnerability"
  aria-describedby="delete-description"
>
  <Trash2 className="h-4 w-4" />
</button>
```

### **Keyboard Navigation:**
```jsx
const handleKeyDown = (event) => {
  if (event.key === 'Enter' || event.key === ' ') {
    event.preventDefault();
    handleClick();
  }
};
```

### **Focus Management:**
```jsx
useEffect(() => {
  if (isOpen) {
    firstInputRef.current?.focus();
  }
}, [isOpen]);
```

---

## 📊 **MÉTRICAS DE UI/UX**

### **Performance:**
- **First Contentful Paint:** < 1.5s
- **Largest Contentful Paint:** < 2.5s
- **Cumulative Layout Shift:** < 0.1
- **First Input Delay:** < 100ms

### **Accessibility:**
- **WCAG 2.1 AA Compliance:** 100%
- **Keyboard Navigation:** Fully supported
- **Screen Reader:** Compatible
- **Color Contrast:** 4.5:1 minimum

### **User Experience:**
- **Task Completion Rate:** 95%
- **User Satisfaction:** 4.5/5
- **Error Rate:** < 2%
- **Time to Complete Task:** < 30 seconds

---

**✅ Diagramas de Interfaz de Usuario Documentados**
**📅 Fecha de Creación: Septiembre 2025**
**👥 Responsable: Equipo de Desarrollo**
