# CloudNativeExams

### This project serves two primary purposes. The first, to continue growing and refining my AWS skillset by constructing something that provides genuine value to both friends and colleagues, in this instance turning a set of bland, JavaScript based, AWS practice exams into a cloud-native, serverless, full-stack application (hosted freely!) 

Features include:
- Persistent Score Saving
  - Records: count of correct answers, time elapsed (these two values determine leaderboard ranking), name and username
- Multiplayer High Score Leader Board
- Personal High Score Board
- Categorized Questions (Determine Areas of Weakness)
- Centralized Navigatation of Exams

Features were implemented using a variety of AWS services:
- Amazon RDS Database (PostgreSQL)
- AWS Lambda Function (Python + AWS Psycopg)
- S3 Static Web Hosting 
- AWS API Gateway

### The second purpose was to gamify the otherwise tiresome process of practice exam taking. Whether you're competitive and want to take the top spot or you just enjoy seeing your progress visualized, it makes the experience at least a little more entertaining.


