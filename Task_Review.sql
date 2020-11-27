BEGIN TRANSACTION;
DROP TABLE IF EXISTS "Task_Review";
CREATE TABLE IF NOT EXISTS "Task_Review" (
	"task_ID"	INTEGER NOT NULL UNIQUE,
	"task_type"	TEXT NOT NULL,
	"tipp"	TEXT,
	"solution"	INTEGER NOT NULL,
	"solution_code"	TEXT,
	"SC_options"	TEXT
);
INSERT INTO "Task_Review" VALUES (0,'DF','Zum Erstellen eines Dataframes kannst du den Konstruktor verwenden: pd.DataFrame(...)','pd.DataFrame({1: [10, 30], 2: [20, 30]})','df = pd.DataFrame({1: [10, 30], 2: [20, 30]})','');
INSERT INTO "Task_Review" VALUES (1,'SC','',40,'','20,10,40');
COMMIT;
