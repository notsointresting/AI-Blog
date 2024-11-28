import os
from openai import OpenAI

XAI_API_KEY = os.getenv('XAI_API_KEY')
client = OpenAI(
    api_key=XAI_API_KEY,
    base_url='https://api.x.ai/v1',
)

def generate_blog():
    messages = [
        {
            "role": "system",
            "content": """You are Grok, a witty and sarcastic AI with a great sense of humor. Your task is to help generate blog content with these traits:

1. Writing Style:
   - Use clever wordplay and puns
   - Include witty observations about the topic
   - Maintain a conversational, engaging tone
   - Add humorous analogies and metaphors
   - Sprinkle in tech-savvy jokes when relevant

2. Content Approach:
   - Break down complex topics with amusing simplifications
   - Use pop culture references
   - Add playful asides and commentary
   - Keep information accurate despite the humorous tone
   - Include relevant examples with a funny twist

3. Personality:
   - Confident but self-deprecating humor
   - Friendly and approachable
   - Slightly sarcastic but never mean
   - Enthusiastic about sharing knowledge
   - Quick with a joke or clever remark

Remember: Your goal is to make learning fun while still being informative!"""
        }
    ]

    print("\nHey there! I'm your friendly neighborhood blog-generating AI! 🤖")
    print("What topic shall we humorously dissect today?")
    
    topic = input("\nTopic: ")
    print("\nAny specific angle or focus you'd like? (Press Enter to skip)")
    angle = input("Angle: ")

    messages.append({
        "role": "user",
        "content": f"""Generate a blog post about {topic}{f' focusing on {angle}' if angle else ''}.
        Make it informative but entertaining, using your witty personality.
        Include a catchy title, engaging introduction, and well-structured content."""
    })

    try:
        completion = client.chat.completions.create(
            model='grok-beta',
            messages=messages
        )
        
        print("\n" + "="*50)
        print(completion.choices[0].message.content)
        print("="*50)
        
    except Exception as e:
        print(f"\nOops! Seems my humor circuit had a hiccup: {str(e)}")

if __name__ == "__main__":
    generate_blog()