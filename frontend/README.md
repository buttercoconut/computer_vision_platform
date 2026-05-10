# Frontend for Computer Vision Platform

## Project Structure
```
frontend/
├─ src/
│  ├─ components/
│  │  ├─ ImageUploader.vue
│  │  └─ ResultViewer.vue
│  ├─ services/
│  │  └─ api.ts
│  ├─ router/
│  │  └─ index.ts
│  ├─ App.vue
│  └─ main.ts
├─ package.json
├─ vite.config.ts
└─ Dockerfile
```

## How to Run
```bash
cd frontend
npm install
npm run dev
```

The app will be available at `http://localhost:5173`. It allows you to upload an image and displays the JSON result returned by the backend.
