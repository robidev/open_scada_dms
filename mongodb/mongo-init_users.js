db = new Mongo().getDB("scada");

db = db.getSiblingDB(process.env.MONGO_USER_DB);

db.createUser({
  user: process.env.MONGO_USER_USERNAME,
  pwd: process.env.MONGO_USER_PASSWORD,
  roles: [
    { role: "readWrite", db: process.env.MONGO_USER_DB }
  ]
});


