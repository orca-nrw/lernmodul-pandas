BEGIN TRANSACTION;
DROP TABLE IF EXISTS "TaskReview";
CREATE TABLE IF NOT EXISTS "TaskReview" (
	"taskID"	INTEGER NOT NULL UNIQUE,
	"taskType"	TEXT NOT NULL,
	"tipp"	TEXT,
	"solutionForReview"	INTEGER NOT NULL,
	"additionalInformation"	TEXT NOT NULL
);
INSERT INTO "TaskReview" VALUES (0,'DFP','Zum Erstellen eines Dataframes kannst du den Konstruktor verwenden: pd.DataFrame(...)','SELECT * FROM netflix_titles;','con = sqlite3.connect(''taskReviewDatabase.db'')
df = pd.read_sql_query(''SELECT * from netflix_titles'', con)
con.close()');
INSERT INTO "TaskReview" VALUES (1,'SC','',40,'20,10,40');

COMMIT;
