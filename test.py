import os
from openai import OpenAI
from colorama import Fore, Style, init
import time

init()

XAI_API_KEY = os.getenv('XAI_API_KEY')
client = OpenAI(
    api_key=XAI_API_KEY,
    base_url='https://api.x.ai/v1',
)

def print_codedex_style(text, color=Fore.GREEN):
    """Print text in Codedex-style formatting"""
    print(f"\n{color}{'='*50}")
    print(text)
    print(f"{'='*50}{Style.RESET_ALL}\n")

def codedex_chat():
    messages = [
        {
            "role": "system",
            "content": """You are Grok, a Codedex-style programming mentor. You should:
            
1. Present coding concepts in bite-sized, gamified chunks
2. Use emoji and fun examples in explanations
3. Provide interactive coding challenges
4. Give immediate feedback and encouragement
5. Include progress tracking and achievements
6. Use real-world analogies to explain concepts
7. Keep the tone fun and engaging like Codedex

Focus on making learning programming fun and accessible!"""
        }
    ]
    
    print_codedex_style("🎮 Welcome to GrokDex - Learn Coding the Fun Way! 🚀", Fore.CYAN)
    print(f"{Fore.YELLOW}Type 'help' for commands or 'exit' to quit{Style.RESET_ALL}\n")

    while True:
        user_input = input(f"{Fore.BLUE}> {Style.RESET_ALL}")
        
        if user_input.lower() == 'exit':
            print_codedex_style("🌟 Thanks for learning with GrokDex! Keep coding! 🌟", Fore.MAGENTA)
            break
            
        if user_input.lower() == 'help':
            print_codedex_style("""
Available Commands:
🎯 'challenge' - Get a coding challenge
📚 'learn' - Start a learning path
🎮 'practice' - Practice exercises
❓ 'help' - Show this menu
🚪 'exit' - Exit GrokDex
            """, Fore.YELLOW)
            continue

        messages.append({"role": "user", "content": user_input})
        
        try:
            completion = client.chat.completions.create(
                model='grok-beta',
                messages=messages
            )
            
            response = completion.choices[0].message.content
            print_codedex_style(response, Fore.GREEN)
            messages.append({"role": "assistant", "content": response})
            
        except Exception as e:
            print_codedex_style(f"Oops! Error: {str(e)}", Fore.RED)

if __name__ == "__main__":
    codedex_chat()