# QuickServe

QuickServe is a comprehensive full-stack service and utility management application built using the MERN stack (Next.js, Node.js, Express, MongoDB).

## Features
- **User:** Browse services, book appointments, track history.
- **Provider:** Manage requests, update status.
- **Admin:** System analytics and management.

## Installation Guide
1. Clone the repository: `git clone https://github.com/yourusername/quickserve.git`
2. **Backend:**
   ```bash
   cd backend
   npm install
   npm run dev
   ```
3. **Frontend:**
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

## Deployment Guide
- **Frontend (Vercel):** Connect your GitHub repository to Vercel and set the root directory to `frontend`.
- **Backend (Render):** Create a new Web Service on Render, connect the repo, set the root directory to `backend`, and use `npm start` as the start command.

## Microservices
- **Payment Service**: A standalone Node.js service running on port 5001 to handle simulated payment processing (located in `microservices/payment-service`).
