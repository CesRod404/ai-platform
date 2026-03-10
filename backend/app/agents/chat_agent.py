from langgraph.graph import StateGraph

def build_agent():

    graph = StateGraph()

    graph.add_node("llm")

    graph.set_entry_point("llm")

    return graph.compile()
