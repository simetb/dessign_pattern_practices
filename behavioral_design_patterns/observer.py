"""
    Observer
    Defines a dependency between objects so that whenever an object changes its state, all its dependents
    are notified
"""

class JobPost:
    def __init__(self, title: str):
        self.title = title

    def get_title(self) -> str:
        return self.title


class Observer:
    def on_job_posted(self, job: JobPost):
        pass


class JobSeeker(Observer):
    def __init__(self, name: str):
        self.name = name

    def on_job_posted(self, job: JobPost):
        # Do something with the job posting
        print(f'Hi {self.name}! New job posted: {job.get_title()}')


class EmploymentAgency:
    def __init__(self):
        self.observers = []

    def notify(self, job_posting: JobPost):
        for observer in self.observers:
            observer.on_job_posted(job_posting)

    def attach(self, observer: Observer):
        self.observers.append(observer)

    def add_job(self, job_posting: JobPost):
        self.notify(job_posting)


# Create subscribers
john_doe = JobSeeker('John Doe')
jane_doe = JobSeeker('Jane Doe')

# Create publisher and attach subscribers
job_postings = EmploymentAgency()
job_postings.attach(john_doe)
job_postings.attach(jane_doe)

# Add a new job and see if subscribers get notified
job_postings.add_job(JobPost('Software Engineer'))

# Output
# Hi John Doe! New job posted: Software Engineer
# Hi Jane Doe! New job posted: Software Engineer
