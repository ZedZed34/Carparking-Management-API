# 🚂 **Railway Deployment - Exact Steps from Screenshot**

## **Following Your Screenshot Instructions:**

---

## **2) Railway Setup**

### **Step 1: Create a new Railway project → Deploy from GitHub → select repo**

1. **Go to Railway.app:**
   - Visit: https://railway.app
   - Click **"Login"** and sign in with GitHub

2. **Create New Project:**
   - Click **"New Project"** (big purple button)
   - Select **"Deploy from GitHub repo"**
   - Find and select your **"Carpark Django API"** repository
   - Click **"Deploy Now"**

### **Step 2: Add Environment Variables**

In your Railway project dashboard, click **"Variables"** tab and add these **exactly**:

#### **Required Variables:**
```
DJANGO_SECRET_KEY = django-insecure-your-very-long-secret-key-here-make-it-50-plus-characters-random
```
```
DJANGO_DEBUG = False
```
```
ALLOWED_HOSTS = *
```
```
CSRF_TRUSTED_ORIGIN = https://your-app-name.railway.app
```
```
DB_SSL_REQUIRED = true
```

**How to add each variable:**
1. Click **"+ New Variable"**
2. Enter **Variable Name** (e.g., `DJANGO_SECRET_KEY`)
3. Enter **Value** (e.g., your secret key)
4. Click **"Add"**
5. Repeat for each variable

### **Step 3: Add Postgres plugin (Railway sets DATABASE_URL automatically)**

1. In your Railway project dashboard
2. Click **"+ New Service"**
3. Select **"Database"**
4. Choose **"PostgreSQL"**
5. Click **"Add PostgreSQL"**
6. ✅ Railway automatically creates `DATABASE_URL` environment variable

### **Step 4: Set build to use Dockerfile (auto-detected)**

1. Go to **"Settings"** tab in your project
2. Under **"Build"** section:
   - Should show **"Dockerfile detected"** ✅
   - If not, check **"Source"** → **"Root Directory"** is `/`
3. Railway will automatically use your `Dockerfile`

---

## **3) GitHub Secrets**

### **In repo → Settings → Secrets → Actions:**

1. **Go to your GitHub repository**
2. Click **"Settings"** (top menu)
3. Click **"Secrets and variables"** (left sidebar)
4. Click **"Actions"** 
5. Click **"New repository secret"**

### **Add this required secret:**

```
Name: RAILWAY_TOKEN
Value: [token from Railway account]
```

**How to get Railway token:**
1. Go to Railway.app → Click your profile → **"Account Settings"**
2. Click **"Tokens"** tab
3. Click **"Create New Token"**
4. Copy the token (you only see it once!)
5. Paste it as the value for `RAILWAY_TOKEN` in GitHub

### **Optional secrets:**

```
Name: DJANGO_SUPERUSER_USERNAME
Value: admin
```

```
Name: DJANGO_SUPERUSER_EMAIL
Value: admin@example.com
```

```
Name: DJANGO_SUPERUSER_PASSWORD
Value: your-secure-password
```

---

## **🎯 Step-by-Step Visual Guide:**

### **Railway Dashboard Setup:**

**1. Environment Variables Tab:**
```
┌─────────────────────────────────────────────────┐
│ Variables                                       │
├─────────────────────────────────────────────────┤
│ + New Variable                                  │
│                                                 │
│ DJANGO_SECRET_KEY = your-secret-key            │
│ DJANGO_DEBUG = False                           │
│ ALLOWED_HOSTS = *                              │
│ CSRF_TRUSTED_ORIGIN = https://your-app.railway.app │
│ DB_SSL_REQUIRED = true                         │
│ DATABASE_URL = postgresql://... (auto-set)     │
└─────────────────────────────────────────────────┘
```

**2. Services Tab:**
```
┌─────────────────────────────────────────────────┐
│ Services                                        │
├─────────────────────────────────────────────────┤
│ 📦 carpark-api (web service)                   │
│ 🗄️ PostgreSQL (database)                       │
└─────────────────────────────────────────────────┘
```

### **GitHub Secrets Setup:**

**Repository Settings → Secrets:**
```
┌─────────────────────────────────────────────────┐
│ Repository secrets                              │
├─────────────────────────────────────────────────┤
│ RAILWAY_TOKEN                  •••••••••••••••  │
│ DJANGO_SUPERUSER_USERNAME      •••••••••••••••  │
│ DJANGO_SUPERUSER_EMAIL         •••••••••••••••  │
│ DJANGO_SUPERUSER_PASSWORD      •••••••••••••••  │
└─────────────────────────────────────────────────┘
```

---

## **🚀 Quick Setup Commands (Copy & Paste):**

### **For Railway Environment Variables:**

**Copy these values exactly:**

1. **DJANGO_SECRET_KEY:**
   ```
   django-insecure-change-this-to-a-real-secret-key-in-production-make-it-long-and-random-50-characters
   ```

2. **DJANGO_DEBUG:**
   ```
   False
   ```

3. **ALLOWED_HOSTS:**
   ```
   *
   ```

4. **CSRF_TRUSTED_ORIGIN:**
   ```
   https://carpark-django-api-production.railway.app
   ```
   *(Replace with your actual Railway app URL)*

5. **DB_SSL_REQUIRED:**
   ```
   true
   ```

---

## **✅ Verification Steps:**

### **After completing setup, check these:**

1. **Railway Dashboard:**
   - ✅ PostgreSQL service running
   - ✅ Web service deployed
   - ✅ Environment variables set
   - ✅ Build logs show success

2. **Test Your App:**
   - ✅ Visit: `https://your-app.railway.app/health/`
   - ✅ Should return: `{"status": "healthy"}`
   - ✅ Visit: `https://your-app.railway.app/api/v1/carparks/`
   - ✅ Should return carpark data

3. **GitHub Actions:**
   - ✅ Go to **"Actions"** tab in your repo
   - ✅ Should see successful deployment runs

---

## **🔧 Troubleshooting:**

### **Common Issues:**

**1. Build Fails:**
- Check Railway build logs
- Verify Dockerfile syntax
- Ensure all files are committed to GitHub

**2. Environment Variables Not Working:**
- Double-check variable names (case-sensitive)
- Verify no extra spaces in values
- Restart the service after adding variables

**3. Database Connection Issues:**
- Ensure PostgreSQL service is running
- Check `DATABASE_URL` is auto-set by Railway
- Verify `DB_SSL_REQUIRED=true`

**4. GitHub Actions Fails:**
- Check `RAILWAY_TOKEN` is correctly set
- Verify token has not expired
- Check Railway CLI installation in actions

---

## **🎉 You're All Set!**

Following these exact steps from your screenshot will get your Carpark Django API deployed to Railway. 

**Your app will be live at:** `https://[your-project-name].railway.app`

**Next:** Go to Railway.app and start with step 1! 🚀
