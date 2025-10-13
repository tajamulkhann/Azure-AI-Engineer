## Function calling
Function calling lets a model decide when to invoke developer-defined tools or APIs by emitting a structured function name and arguments, enabling the app to run real code, fetch data, and return results back to the model for grounded answers.​

### What this notebook does
- Sets up credentials and clients, then defines callable tools (e.g., a weather fetcher) with their input schema so the model can request real data through function calls.​​

- Prompts the agent with a user question; when weather data is needed, the model proposes a function name and arguments, which the app executes, then returns tool output to the model for a final answer.​​

Handles basic control flow: detect tool call, run the function, pass results back, and print the grounded response for the user.​​

### Steps taken
- Imported required SDKs, set up environment variables/credentials, and initialized the AI client/agent for the session.​​

- Defined a weather function interface with parameters (location, date/time) so the model can request precise calls when needed.​​

- Sent a user weather question and captured the model’s tool-call request with structured args.​​

- Executed the weather function, obtained real data, and fed the tool output back to the model for synthesis.​​

- Returned and printed a concise, user-ready weather answer grounded in the fetched data.​​