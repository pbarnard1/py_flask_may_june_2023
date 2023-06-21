# Python PT - outline for Week 7: Tuesday, June 20, 2023

## Reminders:
- For this course, you need the following to pass:
    - Need at least 15 out of 16 core assignments (try to do as many practice assignments as you can)
    - Need at least 11 (preferably 12) out of 16 discussion topics
    - Pass the belt exam with any belt color (have 3 attempts, need to get 15+ core assignments done to be eligible for test)
- Don't forget about the 20-minute rule and Dojo Hall!

## IMPORTANT announcements:
- Make sure when you submit your Flask projects to submit your Pipfile and Pipfile.lock files!  When you submit projects that use a database, make sure you include your .mwb file!  For the exam, you will need to include these 3 files, along with the application itself!
- Code from the belt review project will NOT be pushed to GitHub, and the same with the wireframe
- Important deadlines:
    - Cutoff to *request* an exam code: 8 PM Pacific Tuesday, June 27
    - Cutoff to *unlock the exam* on platform: 11:59 PM Pacific Tuesday, June 27
    - Cutoff to submit needed core assignments and discussion topics: 11:59 PM Pacific Wednesday, June 28

## Outline for today and tomorrow:
- Today:
    - Review what we've done so far:
        - File and folder structure
        - Routes defined
        - Schema file
    - Other cleanup before we dive in:
        - Add logic to ensure only logged in users can access most routes
        - Make sure visible routes return HTML in most cases
    - Add one item with logged in user to database (CREATE)
    - Grab all items with users linked from database (READ all)
- Tomorrow:
    - Grab one item with user linked from database (READ one)
    - Grab user with items linked to them (READ)
    - Edit item in database (UPDATE)
    - Remove item from database (DELETE)