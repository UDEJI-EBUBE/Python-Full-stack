Day 71 — Deploying My Website with Vercel + Managing PostgreSQL with Neon

Today I learnt how to deploy a website using the Vercel website (dashboard),
and how to connect and manage my database using Neon PostgreSQL.

 What I Learnt Today

1. How to Deploy Using the Vercel Website
 - I went to https://vercel.com
 - Logged in with my GitHub account.
 - Clicked “Add New…” → “Project”.
 - Selected the GitHub repository of my project.
 - Vercel automatically detected my framework (Next.js, React, or plain HTML).
 - I clicked “Deploy” and Vercel deployed my website instantly.

2. How Vercel Handles Project Settings
 - I learnt how to set build settings.
 - I saw how Vercel handles automatic deployments for every Git push.
 - I learnt how to check build logs and preview deployments.

3. How I Created a PostgreSQL Database Using Neon
 - I went to https://neon.tech
 - Logged in and created a new PostgreSQL database.
 - Neon gave me a connection string (postgres://user:password@host/dbname).

4. How to Use Neon Database in My Web Project
 - I copied my Neon connection string.
 - I went to my Vercel project dashboard → Settings → Environment Variables.
 - I added:
 DATABASE_URL = postgres://<connection-string>
 - Now my deployed website can connect to Neon securely.

5. How to Run Migrations or Seed Data
 - I learnt that tools like Prisma, Sequelize, Drizzle, or raw SQL 
 can run migrations pointing to the Neon connection string.

6. How to Verify That My App Can Reach the Neon DB
 - I tested queries using SQL clients like psql, TablePlus, or Neon's built-in SQL editor.
 - I confirmed that my deployed Vercel site could read/write to the Neon PostgreSQL database.

Summary:
Today I learnt how to deploy a full website using the Vercel dashboard, and how to create 
and manage a hosted PostgreSQL database using Neon. I also learnt how to add environment 
variables on Vercel so my live website can connect to Neon smoothly. My application is now 
fully deployed online with a working cloud database.
