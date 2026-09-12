import os
from pgzero.rect import Rect
from config import (
    WIDTH, HEIGHT, TITLE,
    COLOR_PRIMARY, COLOR_SECONDARY, COLOR_SCORE, COLOR_DANGER, COLOR_SUCCESS, COLOR_WHITE, COLOR_BLACK,
    FONT_SIZE_TITLE, FONT_SIZE_SUBTITLE, FONT_SIZE_HUD, FONT_SIZE_HUD_VAL, FONT_SIZE_GAME_OVER
)

def get_font():
    if os.path.exists("fonts"):
        files = os.listdir("fonts")
        for f in files:
            if f.endswith(".ttf") or f.endswith(".otf"):
                lower_f = f.lower()
                if f != lower_f:
                    old_path = os.path.join("fonts", f)
                    new_path = os.path.join("fonts", lower_f)
                    try:
                        os.rename(old_path, new_path)
                    except Exception:
                        pass
                    f = lower_f
                return os.path.splitext(f)[0]
    return None

class UIManager:
    @staticmethod
    def draw_menu(screen):
        font = get_font()
        center_x = WIDTH // 2
        center_y = HEIGHT // 2
        
        screen.draw.text(TITLE, center=(center_x, center_y - 100), fontsize=FONT_SIZE_TITLE, color=COLOR_PRIMARY, owidth=2.5, ocolor=COLOR_BLACK, fontname=font)
        screen.draw.text("ivonne lillo", center=(center_x, center_y - 20), fontsize=FONT_SIZE_SUBTITLE, color=COLOR_WHITE, owidth=2.0, ocolor=COLOR_BLACK, fontname=font)
        screen.draw.text("START GAME", center=(center_x, center_y + 80), fontsize=30, color=COLOR_SUCCESS, owidth=1.5, ocolor=COLOR_BLACK, fontname=font)

    @staticmethod
    def draw_hud(screen, player, boss):
        font = get_font()
        center_x = WIDTH // 2
        margin_top = 12
        center_bar_x = center_x - 80

        screen.draw.text("SCORE", (30, margin_top), fontsize=FONT_SIZE_HUD, color=COLOR_SCORE, owidth=1, ocolor=COLOR_BLACK, fontname=font)
        screen.draw.text(f"{player.score}", (30, margin_top + 20), fontsize=FONT_SIZE_HUD_VAL, color=COLOR_PRIMARY, owidth=1.5, ocolor=COLOR_BLACK, fontname=font)

        if boss:
            screen.draw.text("BOSS >", (center_bar_x, margin_top), fontsize=FONT_SIZE_HUD, color=COLOR_DANGER, owidth=1, ocolor=COLOR_BLACK, fontname=font)
            screen.draw.rect(Rect((center_bar_x, margin_top + 24), (160, 16)), color=COLOR_WHITE)
            boss_ratio = max(0, boss.health / boss.max_health)
            screen.draw.filled_rect(Rect((center_bar_x + 2, margin_top + 26), (int(156 * boss_ratio), 12)), color=COLOR_DANGER)
        else:
            screen.draw.text("GOAL: 1000", (center_bar_x, margin_top), fontsize=FONT_SIZE_HUD, color=COLOR_PRIMARY, owidth=1, ocolor=COLOR_BLACK, fontname=font)
            screen.draw.rect(Rect((center_bar_x, margin_top + 24), (160, 16)), color=COLOR_WHITE)
            progress_ratio = min(1.0, player.score / 1000.0)
            screen.draw.filled_rect(Rect((center_bar_x + 2, margin_top + 26), (int(156 * progress_ratio), 12)), color=COLOR_SCORE)

        lives_start_x = WIDTH - 220
        screen.draw.text("LIVES", (lives_start_x, margin_top), fontsize=FONT_SIZE_HUD, color=COLOR_DANGER, owidth=1, ocolor=COLOR_BLACK, fontname=font)
        
        total_lives = max(0, player.lives)
        visible_hearts = min(total_lives, 5)

        for i in range(visible_hearts):
            screen.blit("ui/heart", (lives_start_x + i * 26, margin_top + 22))

        if total_lives > 5:
            extra = total_lives - 5
            screen.draw.text(f"+{extra}", (lives_start_x + 5 * 26 + 4, margin_top + 22), fontsize=FONT_SIZE_HUD, color=COLOR_SECONDARY, owidth=1.5, ocolor=COLOR_BLACK, fontname=font)

    @staticmethod
    def draw_game_over(screen, player):
        font = get_font()
        center_x = WIDTH // 2
        center_y = HEIGHT // 2
        screen.draw.text("MISSION FAILED", center=(center_x, center_y - 50), fontsize=FONT_SIZE_GAME_OVER, color=COLOR_DANGER, owidth=2.5, ocolor=COLOR_BLACK, fontname=font)
        screen.draw.text(f"Puntuacion Final: {player.score}", center=(center_x, center_y + 50), fontsize=22, color=COLOR_SECONDARY, fontname=font)

    @staticmethod
    def draw_victory(screen, player):
        font = get_font()
        center_x = WIDTH // 2
        center_y = HEIGHT // 2
        screen.draw.text("MISSION COMPLETE!", center=(center_x, center_y - 50), fontsize=FONT_SIZE_TITLE, color=COLOR_SUCCESS, owidth=2.5, ocolor=COLOR_BLACK, fontname=font)
        screen.draw.text(f"Puntuacion Final: {player.score}", center=(center_x, center_y + 50), fontsize=22, color=COLOR_WHITE, fontname=font)

