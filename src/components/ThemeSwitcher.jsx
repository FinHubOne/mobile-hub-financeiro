
import { Sun, Moon } from 'lucide-react';

const ThemeSwitcher = ({ theme, toggleTheme }) => {
  return (
    <button onClick={toggleTheme} className="theme-switcher">
      {theme === 'light' ? <Moon size={22} /> : <Sun size={22} />}
    </button>
  );
};

export default ThemeSwitcher;
