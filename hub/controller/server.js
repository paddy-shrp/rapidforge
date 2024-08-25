const path = require("path");
const config = require('./config.json');
const proxy = require('express-http-proxy');
const {auth, requiresAuth } = require("express-openid-connect");
const express = require("express");
const cors = require("cors")

const app = express();

// Authentication

if (isInProduction()) {

  const auth_config = {
    authRequired: false,
    auth0Logout: true,
    secret: config.auth0.client_secret,
    baseURL: config.auth0.client_secret,
    clientID: config.auth0.client_secret,
    issuerBaseURL: config.auth0.client_secret
  };

  app.use(auth(auth_config));

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

const port = config.port;

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});

function isInProduction() {
  return config.state == "PRODUCTION"
}