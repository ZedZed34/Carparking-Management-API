# 🚂 **Railway: Where to Add Environment Variables & PostgreSQL**

## 📍 **Exact Locations in Railway Dashboard**

Based on your current Railway project, here's exactly where to find everything:

---

## **🔧 1. Adding Environment Variables**

### **Step-by-Step Location:**

1. **You're already in the right place!** Your Railway dashboard shows:
   ```
   web-production-06ecb.up.railway.app
   ```

2. **Click on the "Variables" tab** (you can see it in your dashboard):
   ```
   [Deployments] [Variables] [Metrics] [Settings]
                    ↑ CLICK HERE
   ```

3. **Click the "+ New Variable" button** (should be visible in Variables tab)

4. **Add each variable one by one:**

### **📝 Variables to Add (Copy Each Line):**

**Variable 1:**
```
Name: DJANGO_SECRET_KEY
Value: Uan9i8s16ZkrR!rN^vjz5q9xuCR9d9QBNcLYJ!@jvnmerQ3J0eo5ysVUyIclvKau
```

**Variable 2:**
```
Name: DJANGO_DEBUG
Value: False
```

**Variable 3:**
```
Name: ALLOWED_HOSTS
Value: *
```

**Variable 4:**
```
Name: CSRF_TRUSTED_ORIGIN
Value: https://web-production-06ecb.up.railway.app
```

**Variable 5:**
```
Name: RAILWAY_ENVIRONMENT
Value: production
```

---

## **🗄️ 2. Adding PostgreSQL Database**

### **Step-by-Step Location:**

1. **From your current Railway project dashboard**

2. **Look for the "+" button** or **"New Service"** button:
   - Usually in the top-right area
   - Or in the services section
   - Or click the "+" icon in the sidebar

3. **Click "+ New Service"** or **"Add Service"**

4. **Select "Database"** from the menu

5. **Choose "PostgreSQL"**

6. **Click "Add PostgreSQL"** or **"Deploy"**

### **🔍 Visual Guide:**

```
┌─────────────────────────────────────────────┐
│ Railway Project Dashboard                   │
├─────────────────────────────────────────────┤
│                                [+ New Service]│
│ Services:                                   │
│ ┌─────────────┐                            │
│ │ 🌐 web      │                            │
│ │ production  │                            │
│ └─────────────┘                            │
│                                             │
│ Click "+ New Service" above ↑              │
│ Then: Database → PostgreSQL                 │
└─────────────────────────────────────────────┘
```

---

## **📱 Alternative Ways to Find These:**

### **Environment Variables:**
1. **From your dashboard**: web service → **Variables** tab
2. **From sidebar**: Your service → **Variables**
3. **URL**: Should be something like `railway.app/project/your-project/service/web/variables`

### **PostgreSQL Database:**
1. **Main project view**: **+ New Service** button
2. **From sidebar**: **+ Add Service**
3. **Project settings**: **Services** → **Add Service**

---

## **🎯 Quick Navigation:**

### **If you can't find Variables tab:**
1. Make sure you're in the **web service** (not project overview)
2. Look for tabs: `Deployments | Variables | Metrics | Settings`
3. If you don't see tabs, click on your **web service** first

### **If you can't find + New Service:**
1. Go to your **project overview** (not inside a service)
2. Look for **"+"** icon or **"New Service"** button
3. Should be in the top area or sidebar

---

## **🔄 After Adding Variables & Database:**

### **1. Variables Added:**
Your Variables tab should show:
```
DJANGO_SECRET_KEY = •••••••••••••••••••••••••••••••••••••••••••••••••••
DJANGO_DEBUG = False
ALLOWED_HOSTS = *
CSRF_TRUSTED_ORIGIN = https://web-production-06ecb.up.railway.app
RAILWAY_ENVIRONMENT = production
DATABASE_URL = postgresql://... (auto-added by PostgreSQL)
```

### **2. Services Added:**
Your project should show:
```
┌─────────────┐  ┌─────────────┐
│ 🌐 web      │  │ 🗄️ postgres │
│ production  │  │ database    │
└─────────────┘  └─────────────┘
```

### **3. Automatic Redeploy:**
- Railway will automatically redeploy after adding variables
- Wait 2-3 minutes for the redeploy to complete
- Check the **Deployments** tab for progress

---

## **✅ Expected Result:**

After adding variables and PostgreSQL:

1. **Your app will redeploy automatically**
2. **Database connection will be established**
3. **Environment variables will be loaded**
4. **Your API should work at**: `https://web-production-06ecb.up.railway.app/health/`

---

## **🚨 Can't Find These Options?**

### **Try These Steps:**

1. **Refresh your browser**
2. **Click on your project name** at the top
3. **Make sure you're in the right project** (`adorable-courage`)
4. **Check if you have permissions** (should be owner/admin)

### **Screenshot Reference:**
Based on your screenshot, you should see:
- **Project name**: `adorable-courage`
- **Service**: `web` (web-production-06ecb.up.railway.app)
- **Current tabs**: Deployments, Variables, Metrics, Settings

Click **Variables** → **+ New Variable** to start! 🎯
