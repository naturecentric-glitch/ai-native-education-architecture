#!/usr/bin/env python3
"""Quick test of the teach endpoint."""
import asyncio, json, sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.mcp_tools import tool_teach_concept

async def test():
    print("Testing teach for math12.integrals.indefinite...")
    try:
        r = await tool_teach_concept('student-001', 'math12', 'math12.integrals.indefinite')
        if 'error' in r:
            print(f'ERROR: {r["error"]}')
        elif 'lesson' in r:
            print(f'SUCCESS: title = {r["lesson"].get("title","?")}')
            print(f'Keys: {list(r["lesson"].keys())}')
        else:
            print(f'RESULT KEYS: {list(r.keys())}')
    except Exception as e:
        print(f'EXCEPTION: {type(e).__name__}: {e}')

asyncio.run(test())
