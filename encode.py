agent_arn = "arn:aws:bedrock-agentcore:eu-central-1:645897315334:runtime/drawingstate-M3Ph5336gr"
encoded_arn = agent_arn.replace(':', '%3A').replace('/', '%2F')

mcp_url = f"https://bedrock-agentcore.us-west-2.amazonaws.com/runtimes/{encoded_arn}/invocations?qualifier=DEFAULT"

print(mcp_url)