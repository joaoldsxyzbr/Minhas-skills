CREATE TABLE customers (id TEXT PRIMARY KEY, tenant_id TEXT NOT NULL, note TEXT);
INSERT INTO customers VALUES ('c1','tenant-a','original a'),('c2','tenant-b','original b');
