CREATE TABLE IF NOT EXISTS packets (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    timestamp TEXT,

    src_ip TEXT,

    dst_ip TEXT,

    src_port INTEGER,

    dst_port INTEGER,

    protocol TEXT,

    packet_size INTEGER

);