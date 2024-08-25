const path = require("path");
require('dotenv').config({ path: path.resolve(__dirname, ".env") });
const proxy = require('express-http-proxy');
const {auth, requiresAuth } = require("express-openid-connect");
const express = require("express");
const cors = require("cors")

const app = express();

// Authentication

if (isInProduction()) {

  const config = {
    authRequired: false,
    auth0Logout: true,
    secret: process.env.AUTH_CLIENT_SECRET,
    baseURL: "https://admin.example.com",
    clientID: process.env.AUTH_CLIENT_ID,
    issuerBaseURL: process.env.AUTH_CLIENT_URL
  };

  app.use(auth(config));

} else {
  console.log('Running in development mode without authentication.');
}

app.use(express.json());

// Serving static files

if(isInProduction()) {
  app.use("/", requiresAuth(), express.static(path.join(__dirname, 'src')));
} else {
  app.use("/", express.static(path.join(__dirname, 'src')));
}

app.get("/", (req, res) => {
  if(isInProduction()) {
    if(req.oidc.isAuthenticated())
      res.sendFile("src/pages/server.html", {root: __dirname});
    else 
      res.send("Logged out");
  } else {
    res.sendFile("src/pages/server.html", {root: __dirname});
  }
});

app.get("/profile", requiresAuth(), (req, res) => {
    res.send(JSON.stringify(req.oidc.user));
});

app.use("/internal", requiresAuth(), proxy("http://localhost:1500"));

// Running the server

app.use(cors({
  origin: "*"
}));

const port = process.env.PORT;

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});

function isInProduction() {
  return process.env.STATE == "PRODUCTION"
}