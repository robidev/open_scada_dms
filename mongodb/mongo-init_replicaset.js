db = new Mongo().getDB("scada");

try {
  rs.initiate({
    _id: process.env.MONGO_REPLICA_SET_NAME,
    members: [{ _id: 0, host: "mongodb:27017" }]
  });
} catch (e) {
  print("rs.initiate() may already be done");
}
