# Deploying Equity-Sync to Netlify

## Prerequisites
- A GitHub account
- A Netlify account (free at [netlify.com](https://netlify.com))

## Step-by-Step Deployment Guide

### 1. Push Your Code to GitHub
First, make sure your project is pushed to a GitHub repository:

```bash
git add .
git commit -m "Prepare for Netlify deployment"
git push origin main
```

### 2. Deploy to Netlify

#### Option A: Deploy via Netlify UI (Recommended)
1. Go to [netlify.com](https://netlify.com) and sign in
2. Click "Add new site" → "Import an existing project"
3. Connect your GitHub account if not already connected
4. Select your Equity-Sync repository
5. The build settings should be automatically detected:
   - **Build command**: `npm run build`
   - **Publish directory**: `out`
6. Click "Deploy site"

#### Option B: Deploy via Netlify CLI
1. Install Netlify CLI:
   ```bash
   npm install -g netlify-cli
   ```

2. Login to Netlify:
   ```bash
   netlify login
   ```

3. Deploy your site:
   ```bash
   netlify deploy --prod
   ```

### 3. Custom Domain (Optional)
After deployment, you can:
1. Go to your site settings in Netlify
2. Navigate to "Domain management"
3. Add your custom domain

### 4. Environment Variables (If Needed)
If your app uses environment variables:
1. Go to Site settings → Environment variables
2. Add any required environment variables

## Configuration Files Added

- `netlify.toml`: Netlify configuration file
- Updated `next.config.js`: Configured for static export
- `.gitignore`: Updated to exclude build artifacts

## Build Process
The deployment will:
1. Install dependencies (`npm install`)
2. Build the project (`npm run build`)
3. Serve the static files from the `out` directory

## Troubleshooting
- If the build fails, check the build logs in Netlify
- Ensure all dependencies are in `package.json`
- Verify that the `out` directory is generated after running `npm run build` locally

Your site will be live at a URL like: `https://your-site-name.netlify.app` 