from genai.schema._api import BaseMessage, ChatRole


class HumanMessage(BaseMessage):
    role: ChatRole = ChatRole.USER


class SystemMessage(BaseMessage):
    role: ChatRole = ChatRole.SYSTEM


class AIMessage(BaseMessage):
    role: ChatRole = ChatRole.ASSISTANT


class ToolMessage(BaseMessage):
    role: ChatRole = ChatRole.USER

__all__ = ["HumanMessage", "SystemMessage", "AIMessage", "ToolMessage"]
