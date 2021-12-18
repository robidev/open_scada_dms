db.createUser(
        {
            user: "aaa",
            pwd: "bbb",
            roles: [
                {
                    role: "readWrite",
                    db: "scada"
                }
            ]
        }
);
db = new Mongo().getDB("scada");
db.createCollection("rtu_list");
db.createCollection("data_timeseries");
db.rtu_list.insert([
    { "RTU": "127.0.0.1:2404", "enabled":1, "IFS":"IFS_A" },
    { "RTU": "127.0.0.1:2405", "enabled":0, "IFS":"IFS_A" },
    { "RTU": "127.0.0.1:2406", "enabled":1, "IFS":"IFS_B" },
]);
