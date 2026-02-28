# MinServe

A minimalist gateway server on top of an AI/LLM Inference backend; for educational purposes.

**Repository description:** Set in `.git/description` (e.g. for Gitweb or short clone blurbs).

## Running locally

1. **Create a virtual environment and install dependencies** with [uv](https://docs.astral.sh/uv/):

   ```bash
   uv venv
   uv sync
   ```

2. **Run the gateway server** by executing the main module:

   ```bash
   uv run python app/main.py
   ```

   Or activate the virtual environment and run:

   ```bash
   source .venv/bin/activate   # On Windows: .venv\Scripts\activate
   python app/main.py
   ```

The server will start (default port is from your config); the root endpoint is at `/` and the chat completions endpoint at `/v1/chat/completions`.
Set an environment variable for `PORT` or `BACKEND_URL`. Currently this gateway just responds with the last message in the `POST` request to `/v1/chat/completions`.
It will be extended further.
