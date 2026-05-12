# GazeDecoder

## Project Overview
UsabilityReq is a comprehensive platform for analyzing and researching usability requirements. It includes backend, frontend, data processing, and analysis notebooks.

## Directory Structure

- `backend/`: Backend service based on Flask, responsible for data processing and API provision.
  - `app/`: Main application module, including configuration and routes.
  - `lib/`: Backend libraries and third-party dependencies.
  - `utils/`: Data analysis and eye-tracking tools.
- `frontend/`: Frontend interface based on Vite + Vue, provides user interaction.
- `data/`: Main data directory, contains AOI regions, analysis results, raw and processed data.
- The `data/DataAnalysis/` subfolder includes:
  - `AOI_issue.csv`: AOI (Area of Interest) issue records for analysis.
  - `Patterns.json`: Stores mined patterns from gaze or usability data.
  - `pattern_mining.ipynb`: Jupyter notebook for pattern mining and analysis workflows.

## Backend
The backend uses the Flask framework. Main features include:
- Data analysis and processing (e.g., eye-tracking, session tools)
- API provision for frontend usage
- Configuration and extension support

To start the backend:
```bash
cd backend
python run.py
```

## Frontend
The frontend is based on Vite. Main features include:
- User interface display
- Data visualization
- Interaction with backend APIs

To start the frontend:
```bash
cd frontend
npm install
npm run dev
```

## Main Dependencies
- Python: Flask, pandas, numpy, etc.
- Node.js: Vite, Vue, ECharts, etc.