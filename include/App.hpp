#ifndef APP_H
#define APP_H
#include <SFML/Graphics.hpp>
#include <SFML/System.hpp>
#include "Player.hpp"

class App final
{
    private:
        App();
        App( const App & _app) = delete;

        std::unique_ptr<sf::RenderWindow> m_window;


    public:
        void operator=(const App &) = delete;
        static App & getInstance()
        {
            static App _app;
            return _app;
        }
        void run();
};

#endif // APP_H
