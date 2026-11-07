
from model.request import Request
import base64
from langchain.messages import HumanMessage
from agent.graph import model

async def analysis(data:Request):
    content_block = [
            {
                "type":"text",
                "text": data.prompt
            }
    ]

    if data.image is not None:
        content = await data.image.read()
        base_64 = base64.b64encode(content).decode('utf-8')
        content_block.append({
            "type":"image",
            "base64":base_64,
            "mime_type": data.image.content_type
        })
        await data.image.close()



    message = HumanMessage(
        content=content_block
    )

    config={"configurable":{"thread_id":data.thread_id}}

    response = await model.ainvoke({"messages":message},config=config)

    last_msg = response["messages"][-1]
    if hasattr(last_msg, "text") and last_msg.text:
        return last_msg.text
    return last_msg.content