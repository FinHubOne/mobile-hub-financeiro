import React from 'react';
import { Sun, Moon } from 'lucide-react';

const ThemeSwitcher = ({ theme, toggleTheme }) => {
  return (
    <button
      onClick={toggleTheme}
      className="p-2 rounded-full text-blue-100 dark:text-blue-200 hover:bg-white/20 dark:hover:bg-white/10 transition-colors duration-200"
    >
      {theme === 'light' ? <Moon size={22} /> : <Sun size={22} />}
    </button>
  );
};

export default ThemeSwitcher;
