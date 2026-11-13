from langchain_google_genai import ChatGoogleGenerativeAI


from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()

chatModel = ChatGoogleGenerativeAI(model = "gemini-3.5-flash-lite")
# Using Pydantic
class ReviewPydantic(BaseModel):
    summary: str
    sentiment: str
    rating : float = Field(ge = 0, le= 10, default=5, description="Rating of the product in the range of 0 to 10.")



# using Typed Dict

structured_model = chatModel.with_structured_output(ReviewPydantic)


result = structured_model.invoke("The monitor hardware is not working. half screen is black. I rate it 1 star")

print(result)

