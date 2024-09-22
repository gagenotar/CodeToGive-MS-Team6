import logging
import os
from typing import List

from qdrant_client import QdrantClient

from scripts.utils import find_path, read_json

# Get the logger
logger = logging.getLogger(__name__)

# Set the logging level
logger.setLevel(logging.INFO)


# cwd = find_path("Resume-Matcher")
# READ_RESUME_FROM = os.path.join(cwd, "Data", "Processed", "Resumes/")
# READ_JOB_DESCRIPTION_FROM = os.path.join(cwd, "Data", "Processed", "JobDescription/")

cwd = find_path("Team-6-C2G")
READ_RESUME_FROM = os.path.join(cwd, "Backend", "Resume-Matcher", "Data", "Processed", "Resumes\\")
READ_JOB_DESCRIPTION_FROM = os.path.join(cwd, "Backend", "Resume-Matcher", "Data", "Processed", "JobDescription\\")

def get_score(resume_string, job_description_string):
    """
    The function `get_score` uses QdrantClient to calculate the similarity score between a resume and a
    job description.

    Args:
      resume_string: The `resume_string` parameter is a string containing the text of a resume. It
    represents the content of a resume that you want to compare with a job description.
      job_description_string: The `get_score` function you provided seems to be using a QdrantClient to
    calculate the similarity score between a resume and a job description. The function takes in two
    parameters: `resume_string` and `job_description_string`, where `resume_string` is the text content
    of the resume and

    Returns:
      The function `get_score` returns the search result obtained by querying a QdrantClient with the
    job description string against the resume string provided.
    """
    logger.info("Started getting similarity score")

    documents: List[str] = [resume_string]
    client = QdrantClient(":memory:")
    client.set_model("BAAI/bge-base-en")

    client.add(
        collection_name="demo_collection",
        documents=documents,
    )

    search_result = client.query(
        collection_name="demo_collection", query_text=job_description_string
    )
    logger.info("Finished getting similarity score")
    return search_result


def custom_test():
    # To give your custom resume use this code
    resume_dict = read_json(
        READ_RESUME_FROM
        + "resume_Justis Nazirbage Resume Summer 2024.pdfafea8a26-c07a-4fa4-89ee-c9f908c8e58a.json"
    )
    job_dict = read_json(
        READ_JOB_DESCRIPTION_FROM
        + "job_description_job_desc_front_end_engineer.pdf8a898565-cd5a-4f89-9d95-b45aff7b909f.json"
    )
    resume_keywords = resume_dict["extracted_keywords"]
    job_description_keywords = job_dict["extracted_keywords"]

    resume_string = " ".join(resume_keywords)
    jd_string = " ".join(job_description_keywords)
    final_result = get_score(resume_string, jd_string)
    for r in final_result:
        print(r.score)


# if __name__ == "__main__":
#     custom_test()
