from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict , Annotated

from dotenv import load_dotenv


load_dotenv()

chatModel = ChatGoogleGenerativeAI(model = "gemini-3.5-flash-lite")


# using Typed Dict
class Review(TypedDict):
    summary : Annotated[str,"A brief summary for the review"]
    sentiment : Annotated[str,"Return a sentiment around the review as positive , negative or neutral"]

structured_model = chatModel.with_structured_output(Review)


result = structured_model.invoke("The monitor hardware is not working. half screen is black.")

print(result)

