# 🚂 **Railway Quick Setup - Copy & Paste Values**

## **Step-by-Step from Your Screenshot:**

---

## **2) Railway Setup**

### **✅ Copy These Environment Variables:**

**Go to Railway.app → Your Project → Variables → + New Variable**

```env
DJANGO_SECRET_KEY
Uan9i8s16ZkrR!rN^vjz5q9xuCR9d9QBNcLYJ!@jvnmerQ3J0eo5ysVUyIclvKau

DJANGO_DEBUG
False

ALLOWED_HOSTS
*

CSRF_TRUSTED_ORIGIN
https://your-app-name.railway.app

DB_SSL_REQUIRED
true
```

**Replace `your-app-name` with your actual Railway domain!**

---

## **3) GitHub Secrets**

### **✅ Add These Secrets:**

**Go to GitHub → Your Repo → Settings → Secrets and variables → Actions**

1. **Required:**
   ```
   Name: RAILWAY_TOKEN
   Value: [Get from Railway.app → Account → Tokens]
   ```

2. **Optional (for admin user):**
   ```
   Name: DJANGO_SUPERUSER_USERNAME
   Value: admin
   
   Name: DJANGO_SUPERUSER_EMAIL
   Value: admin@yourapp.com
   
   Name: DJANGO_SUPERUSER_PASSWORD
   Value: SecurePassword123!
   ```

---

## **🎯 Exact Click Path:**

### **Railway Setup:**
1. **Railway.app** → Login with GitHub
2. **"New Project"** → **"Deploy from GitHub repo"**
3. Select **"Carpark Django API"** → **"Deploy Now"**
4. **"+ New Service"** → **"Database"** → **"PostgreSQL"**
5. **"Variables"** tab → Add environment variables above
6. **"Settings"** → Should show **"Dockerfile detected"** ✅

### **GitHub Setup:**
1. **GitHub.com** → Your repository
2. **"Settings"** → **"Secrets and variables"** → **"Actions"**
3. **"New repository secret"** → Add `RAILWAY_TOKEN`
4. Get token from: **Railway.app → Profile → Account Settings → Tokens**

---

## **✅ Final Checklist:**

### **Railway Project:**
- [ ] PostgreSQL database added
- [ ] All 5 environment variables set
- [ ] Dockerfile detected for build
- [ ] Domain assigned (like `xyz.railway.app`)

### **GitHub Repository:**
- [ ] `RAILWAY_TOKEN` secret added
- [ ] Optional superuser secrets added
- [ ] Actions tab shows green checkmarks

### **Test Your Deployment:**
- [ ] `https://your-app.railway.app/health/` returns `{"status": "healthy"}`
- [ ] `https://your-app.railway.app/api/v1/carparks/` returns data
- [ ] `https://your-app.railway.app/admin/` shows Django admin

---

## **🚀 Ready to Deploy!**

Your project is already configured with:
- ✅ `Dockerfile` - Production ready
- ✅ `railway.json` - Railway config
- ✅ `.github/workflows/deploy.yml` - CI/CD
- ✅ All dependencies and settings

**Just follow the steps above and you'll be live!** 🎉
