import sqlite3
from typing import Tuple


class RankingsDAO:
    def __init__(self, db_file: str = "game.db"):
        self.db_file = db_file
        self._create_table()

    def _create_table(self) -> None:
        try:
            with sqlite3.connect(self.db_file) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS rankings (
                        nome_musica TEXT NOT NULL,
                        id_jogador INTEGER NOT NULL,
                        pontuacao INTEGER NOT NULL,
                        PRIMARY KEY (nome_musica, id_jogador),
                        FOREIGN KEY (id_jogador) REFERENCES players(id)
                            ON DELETE CASCADE
                    )
                ''')
                conn.commit()
        except sqlite3.Error as e:
            raise ValueError(e)

    def add_ranking(self, nome_musica: str, id_jogador: int, pontuacao: int) -> None:
        try:
            with sqlite3.connect(self.db_file) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT OR REPLACE INTO rankings (nome_musica, id_jogador, pontuacao)
                    VALUES (?, ?, ?)
                ''', (nome_musica, id_jogador, pontuacao))
                conn.commit()
        except sqlite3.Error as e:
            raise ValueError(f"Erro ao adicionar ranking: {e}")

    def get_rankings_by_music(self, nome_musica: str) -> list[Tuple[str, str, int]]:
        try:
            with sqlite3.connect(self.db_file) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT r.nome_musica, p.nickname, r.pontuacao
                    FROM rankings r
                    INNER JOIN players p ON r.id_jogador = p.id
                    WHERE r.nome_musica = ?
                    ORDER BY r.pontuacao DESC
                ''', (nome_musica,))
                return cursor.fetchall()
        except sqlite3.Error as e:
            raise ValueError(f"Erro ao obter ranking: {e}")

    def get_ranking_by_music(self, nome_musica: str, id_jogador: int) -> Tuple[str, str, int]:
        try:
            with sqlite3.connect(self.db_file) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT r.nome_musica, p.nickname, r.pontuacao
                    FROM rankings r
                    INNER JOIN players p ON r.id_jogador = p.id
                    WHERE r.nome_musica = ?
                    AND r.id_jogador = ?
                    ORDER BY r.pontuacao DESC
                ''', (nome_musica, id_jogador))
                return cursor.fetchone()
        except sqlite3.Error as e:
            raise ValueError(f"Erro ao obter ranking: {e}")

    def get_player_rankings(self, id_jogador: int) -> list[Tuple[str, str, int]]:
        try:
            with sqlite3.connect(self.db_file) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT r.nome_musica, p.nickname, r.pontuacao
                    FROM rankings r
                    INNER JOIN players p ON r.id_jogador = p.id
                    WHERE r.id_jogador = ?
                    ORDER BY r.pontuacao DESC
                ''', (id_jogador,))
                return cursor.fetchall()
        except sqlite3.Error as e:
            raise ValueError(f"Erro ao obter rankings do jogador: {e}")

    def get_all_rankings(self) -> list[Tuple[str, str, int]]:
        try:
            with sqlite3.connect(self.db_file) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT r.nome_musica, p.nickname, r.pontuacao
                    FROM rankings r
                    INNER JOIN players p ON r.id_jogador = p.id
                    ORDER BY r.pontuacao DESC
                ''')
                return cursor.fetchall()
        except sqlite3.Error as e:
            raise ValueError(f"Erro ao obter todos os rankings: {e}")

    def delete_ranking(self, nome_musica: str, id_jogador: int) -> bool:
        try:
            with sqlite3.connect(self.db_file) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    DELETE FROM rankings 
                    WHERE nome_musica = ? AND id_jogador = ?
                ''', (nome_musica, id_jogador))
                conn.commit()
                return cursor.rowcount > 0
        except sqlite3.Error as e:
            raise ValueError(f"Erro ao excluir ranking: {e}")

    def get_top_rankings_by_music(self, nome_musica: str, limit: int = 10) -> list[Tuple[str, str, int]]:
        try:
            with sqlite3.connect(self.db_file) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT r.nome_musica, p.nickname, r.pontuacao
                    FROM rankings r
                    INNER JOIN players p ON r.id_jogador = p.id
                    WHERE r.nome_musica = ?
                    ORDER BY r.pontuacao DESC
                    LIMIT ?
                ''', (nome_musica, limit))
                return cursor.fetchall()
        except sqlite3.Error as e:
            raise ValueError(f"Erro ao obter top rankings: {e}")