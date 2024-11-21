import sqlite3
from typing import Optional, Tuple


class PlayerDAO:
    def __init__(self, db_file: str = "game.db"):
        self.db_file = db_file
        self._create_table()

    def _create_table(self) -> None:
        try:
            with sqlite3.connect(self.db_file) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS players (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nickname TEXT UNIQUE NOT NULL
                    )
                ''')
                conn.commit()
        except sqlite3.Error as e:
            raise ValueError(e)

    def create_player(self, nickname: str) -> Optional[int]:
        try:
            with sqlite3.connect(self.db_file) as conn:
                cursor = conn.cursor()
                cursor.execute('INSERT INTO players (nickname) VALUES (?)', (nickname,))
                conn.commit()
                return cursor.lastrowid
        except sqlite3.IntegrityError:
            raise ValueError(f"Jogador com o nickname {nickname} já existe")
        except sqlite3.Error as e:
            raise ValueError(f"Erro ao criar jogador: {e}")

    def get_player_by_id(self, player_id: int) -> Optional[Tuple[int, str]]:
        try:
            with sqlite3.connect(self.db_file) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT id, nickname FROM players WHERE id = ?', (player_id,))
                result = cursor.fetchone()
                return result if result else None
        except sqlite3.Error as e:
            raise ValueError(f"Erro ao obter jogador: {e}")

    def get_player_by_nickname(self, nickname: str) -> Optional[Tuple[int, str]]:
        try:
            with sqlite3.connect(self.db_file) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT id, nickname FROM players WHERE nickname = ?', (nickname,))
                result = cursor.fetchone()
                return result if result else None
        except sqlite3.Error as e:
            raise ValueError(f"Erro ao obter jogador: {e}")

    def update_player(self, player_id: int, new_nickname: str) -> bool:
        try:
            with sqlite3.connect(self.db_file) as conn:
                cursor = conn.cursor()
                cursor.execute('UPDATE players SET nickname = ? WHERE id = ?',
                               (new_nickname, player_id))
                conn.commit()
                return cursor.rowcount > 0
        except sqlite3.IntegrityError:
            raise ValueError(f"Jogador com o nickname {new_nickname} já existe")
        except sqlite3.Error as e:
            raise ValueError(f"Erro ao atualizar jogador: {e}")

    def delete_player(self, player_id: int) -> bool:
        try:
            with sqlite3.connect(self.db_file) as conn:
                cursor = conn.cursor()
                cursor.execute('DELETE FROM players WHERE id = ?', (player_id,))
                conn.commit()
                return cursor.rowcount > 0
        except sqlite3.Error as e:
            raise ValueError(f"Erro ao excluir jogador: {e}")

    def get_all_players(self) -> list[Tuple[int, str]]:
        try:
            with sqlite3.connect(self.db_file) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT id, nickname FROM players')
                return cursor.fetchall()
        except sqlite3.Error as e:
            raise ValueError(f"Erro ao obter todos os jogadores: {e}")
