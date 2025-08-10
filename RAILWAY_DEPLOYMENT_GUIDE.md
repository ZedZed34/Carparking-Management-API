# 🚂 **Railway Deployment Guide - Step by Step**

Based on your screenshot, here's exactly how to complete the Railway deployment setup for your Carpark Django API.

---

## 🎯 **Step-by-Step Railway Deployment:**

### **2) Railway Setup**

#### **Step 1: Create a New Railway Project**
1. Go to [Railway.app](https://railway.app)
2. Sign in with your GitHub account
3. Click **"New Project"**
4. Select **"Deploy from GitHub repo"**
5. Choose your repository: `Carpark Django API` or similar
6. Click **"Deploy Now"**

#### **Step 2: Add Environment Variables**
In your Railway project dashboard, go to **Variables** tab and add these:

```env
DJANGO_SECRET_KEY=your-super-secret-production-key-here-make-it-long-and-random
DJANGO_DEBUG=False
ALLOWED_HOSTS=*
CSRF_TRUSTED_ORIGIN=https://your-app-name.railway.app
DB_SSL_REQUIRED=true
```

**Important Notes:**
- Replace `your-app-name` with your actual Railway app domain
- Generate a strong secret key (50+ characters, random)
- Keep `ALLOWED_HOSTS=*` for Railway (it handles the routing)

#### **Step 3: Add PostgreSQL Plugin**
1. In your Railway project, click **"New Service"**
2. Select **"Database"** 
3. Choose **"PostgreSQL"**
4. Railway will automatically set the `DATABASE_URL` environment variable

#### **Step 4: Set Build Configuration**
1. Go to **Settings** tab in your Railway project
2. Under **"Build"** section:
   - **Build Command**: (leave empty - Dockerfile handles this)
   - **Start Command**: (leave empty - Dockerfile handles this)
3. Railway will auto-detect your `Dockerfile` ✅

---

### **3) GitHub Secrets Setup**

#### **Step 1: Get Railway API Token**
1. Go to [Railway Account Settings](https://railway.app/account/tokens)
2. Click **"Create New Token"**
3. Copy the token (you'll only see it once!)

#### **Step 2: Add Secrets to GitHub Repository**
1. Go to your GitHub repository
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **"New repository secret"** and add these:

**Required Secret:**
```
Name: RAILWAY_TOKEN
Value: your-railway-api-token-from-step-1
```

**Optional Secrets (for superuser creation):**
```
Name: DJANGO_SUPERUSER_USERNAME
Value: admin

Name: DJANGO_SUPERUSER_EMAIL  
Value: admin@yourdomain.com

Name: DJANGO_SUPERUSER_PASSWORD
Value: your-secure-admin-password
```

---

## 📋 **Complete Environment Variables Checklist:**

### **✅ Required Railway Environment Variables:**

| Variable | Value | Purpose |
|----------|--------|---------|
| `DJANGO_SECRET_KEY` | `long-random-string-50+-chars` | Django security |
| `DJANGO_DEBUG` | `False` | Production mode |
| `ALLOWED_HOSTS` | `*` | Railway routing |
| `CSRF_TRUSTED_ORIGIN` | `https://your-app.railway.app` | CSRF protection |
| `DB_SSL_REQUIRED` | `true` | Database security |
| `DATABASE_URL` | *(Auto-set by PostgreSQL plugin)* | Database connection |

### **✅ Optional Railway Environment Variables:**
| Variable | Value | Purpose |
|----------|--------|---------|
| `DJANGO_SUPERUSER_USERNAME` | `admin` | Auto-create admin user |
| `DJANGO_SUPERUSER_EMAIL` | `admin@example.com` | Admin email |
| `DJANGO_SUPERUSER_PASSWORD` | `secure-password` | Admin password |

---

## 🚀 **Detailed Step-by-Step Instructions:**

### **Part 1: Railway Project Setup**

1. **Create Project:**
   ```
   Railway Dashboard → New Project → Deploy from GitHub → Select your repo
   ```

2. **Add PostgreSQL:**
   ```
   Project Dashboard → New Service → Database → PostgreSQL
   ```
   ✅ This automatically creates `DATABASE_URL`

3. **Configure Environment Variables:**
   ```
   Project Dashboard → Variables → Add Variable
   ```
   
   Add each variable from the table above:
   - Click **"+ Add Variable"**
   - Enter **Name** and **Value**
   - Click **"Add"**

4. **Verify Dockerfile Detection:**
   ```
   Project Dashboard → Settings → Build
   ```
   ✅ Should show "Dockerfile detected" or similar

### **Part 2: GitHub Secrets Setup**

1. **Get Railway Token:**
   ```
   Railway → Account → API Tokens → Create New Token
   ```
   📋 Copy the token immediately!

2. **Add to GitHub:**
   ```
   GitHub Repo → Settings → Secrets and variables → Actions
   ```
   
   Add secrets:
   - `RAILWAY_TOKEN` = your-api-token
   - Optional: superuser credentials

### **Part 3: Verify Deployment**

1. **Check Build Logs:**
   ```
   Railway Project → Deployments → View Logs
   ```

2. **Test Endpoints:**
   ```
   https://your-app.railway.app/health/
   https://your-app.railway.app/api/v1/carparks/
   https://your-app.railway.app/admin/
   ```

---

## 🔧 **Your Project-Specific Settings:**

Based on your current setup, here are the exact values you should use:

### **Environment Variables for Your Project:**
```env
# Required
DJANGO_SECRET_KEY=generate-a-long-random-string-here-50plus-characters
DJANGO_DEBUG=False
ALLOWED_HOSTS=*
CSRF_TRUSTED_ORIGIN=https://carpark-api-production.railway.app
DB_SSL_REQUIRED=true

# Optional (for admin user)
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@carpark-api.com
DJANGO_SUPERUSER_PASSWORD=secure-admin-password-123
```

### **Your Deployment Files Status:**
- ✅ `Dockerfile` - Production ready
- ✅ `railway.json` - Railway configuration
- ✅ `Procfile` - Process definitions
- ✅ `.github/workflows/deploy.yml` - CI/CD pipeline
- ✅ `requirements.txt` - Dependencies
- ✅ All configurations verified and tested

---

## 🎯 **Quick Setup Commands (for reference):**

If you want to test locally first:
```bash
# Set environment variables locally
set DJANGO_SECRET_KEY=test-key-for-local
set DJANGO_DEBUG=False
set ALLOWED_HOSTS=localhost,127.0.0.1
set DATABASE_URL=postgresql://user:pass@localhost:5432/db

# Test with Docker
docker build -t carpark-api .
docker run -p 8000:8000 --env-file .env carpark-api
```

---

## 🚨 **Important Notes:**

### **Security:**
- ⚠️ **Never commit secrets to Git**
- ✅ Use Railway environment variables for production
- ✅ Generate a strong `DJANGO_SECRET_KEY` (50+ characters)

### **Domain Setup:**
- Railway will assign a domain like `carpark-api-production.railway.app`
- Update `CSRF_TRUSTED_ORIGIN` with your actual domain
- You can set a custom domain in Railway settings

### **Database:**
- PostgreSQL plugin creates the database automatically
- Data persists between deployments
- You can view database info in Railway dashboard

---

## ✅ **Verification Checklist:**

After deployment, verify these work:

- [ ] **Health Check**: `https://your-app.railway.app/health/`
- [ ] **API Endpoint**: `https://your-app.railway.app/api/v1/carparks/`
- [ ] **Admin Panel**: `https://your-app.railway.app/admin/`
- [ ] **Web Interface**: `https://your-app.railway.app/home/`
- [ ] **Database**: Data loads and persists
- [ ] **CI/CD**: GitHub Actions deploy successfully

---

## 🎉 **You're Ready to Deploy!**

Your project is already configured with all the necessary files. Just follow the Railway setup steps above, and your Carpark Django API will be live on the internet! 🚀

**Next Step**: Go to [Railway.app](https://railway.app) and start with "New Project" → "Deploy from GitHub"
