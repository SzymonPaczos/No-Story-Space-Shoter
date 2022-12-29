#include "App.hpp"

App::App()
{
    m_window = std::make_unique<sf::RenderWindow>();
    m_window->create(sf::VideoMode(800, 600), "Space Shooter");
}
void App::run()
{

    sf::Time timeLastUpdate = sf::Time::Zero;
    sf::Clock gameClock;
    const sf::Time stepTime = sf::seconds(1.f/60.f);

    while (m_window->isOpen())
    {
        sf::Time time = gameClock.restart();
        timeLastUpdate += time;
        while(timeLastUpdate > stepTime)
        {
            sf::Event event;
            while (m_window->pollEvent(event))
            {
                if (event.type == sf::Event::Closed)m_window->close();
            }
            timeLastUpdate -= stepTime;
        }
        m_window->clear();
       /////Drawing...
        m_window->display();
    }


}
