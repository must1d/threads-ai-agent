import boto3
from pathlib import Path

from strands import Agent
from strands.models import BedrockModel
from strands_tools.browser import LocalChromiumBrowser

CLAUDE_OPUS_4_5_V1 = "anthropic.claude-opus-4-5-20251101-v1:0"
SYSTEM_PROMPT_PATH = Path(__file__).parent / "system_prompt.txt"


def create_bedrock_model() -> BedrockModel:
    return BedrockModel(
        boto_session=boto3.Session(),
        model_id=f"us.{CLAUDE_OPUS_4_5_V1}",
    )


def create_agent() -> Agent:
    browser = LocalChromiumBrowser()
    system_prompt = SYSTEM_PROMPT_PATH.read_text()

    return Agent(
        model=create_bedrock_model(),
        system_prompt=system_prompt,
        tools=[browser.browser],
    )
