from __init__ import CURSOR, CONN


class Department:

    def __init__(self, name, location, id=None):
        self.id = id
        self.name = name
        self.location = location

    def __repr__(self):
        return f"<Department {self.id}: {self.name}, {self.location}>";

    @classmethod
    def create_table(cls):
        CURSOR.execute(
            "CREATE TABLE IF NOT EXISTS departments (id INTEGER PRIMARY KEY, name TEXT, location TEXT);");
        CONN.commit();
        return None;

    @classmethod
    def create(cls, name, location):
        department = cls(name, location);
        department.save();
        return department;

    @classmethod
    def drop_table(cls):
        CURSOR.execute("DROP TABLE IF EXISTS departments;");
        CONN.commit();
        return None;

    def save(self):
        CURSOR.execute("INSERT INTO departments (name, location) VALUES (?, ?)",
                       (self.name, self.location));
        CONN.commit();
        self.id = CURSOR.lastrowid;
        return None;

    def update(self):
        CURSOR.execute("UPDATE departments SET name = ?, location = ? WHERE id = ?",
                       (self.name, self.location, self.id));
        CONN.commit();
        return None;

    def delete(self):
        CURSOR.execute("DELETE FROM departments WHERE id = ?", (self.id,));
        CONN.commit();
        return None;
