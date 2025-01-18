import json
from datetime import datetime
from typing import Dict, List

class UserManager:
    def __init__(self, filename: str = 'users.json'):
        self.filename = filename
        self.users = self._load_users()

    def _load_users(self) -> Dict:
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def _save_users(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self.users, file, ensure_ascii=False, indent=2)

    def add_user(self, user_id: int, username: str = None, first_name: str = None):
        if str(user_id) not in self.users:
            self.users[str(user_id)] = {
                'username': username,
                'first_name': first_name,
                'joined_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'last_activity': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'message_count': 0
            }
        self._save_users()

    def update_user_activity(self, user_id: int):
        if str(user_id) in self.users:
            self.users[str(user_id)]['last_activity'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.users[str(user_id)]['message_count'] += 1
            self._save_users()

    def get_all_users(self) -> List[Dict]:
        return [
            {
                'user_id': user_id,
                **user_data
            }
            for user_id, user_data in self.users.items()
        ]

    def get_user_stats(self) -> str:
        total_users = len(self.users)
        total_messages = sum(user['message_count'] for user in self.users.values())
        
        stats = f"📊 Статистика бота:\n\n"
        stats += f"👥 Всего пользователей: {total_users}\n"
        stats += f"💬 Всего сообщений: {total_messages}\n\n"
        stats += "🏆 Топ-5 активных пользователей:\n"
        
        # Сортируем пользователей по количеству сообщений
        sorted_users = sorted(
            self.users.items(), 
            key=lambda x: x[1]['message_count'], 
            reverse=True
        )[:5]
        
        for i, (user_id, data) in enumerate(sorted_users, 1):
            username = data['username'] or data['first_name'] or f"User{user_id}"
            stats += f"{i}. @{username}: {data['message_count']} сообщений\n"
            
        return stats 