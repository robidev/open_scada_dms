db.getCollectionNames().forEach(name => {
  const docs = db[name].find().toArray();

  docs.forEach(doc => delete doc._id);

  print(`db.${name}.insertMany(${JSON.stringify(docs)});`);
});