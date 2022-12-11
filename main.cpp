#include <SFML/Graphics.hpp>
#include <SFML/System.hpp>

int main()
{
    sf::RenderWindow window(sf::VideoMode(1280,960), "SFML works!");

    sf::Time timeLastUpdate = sf::Time::Zero;
    sf::Clock gameClock;
    const sf::Time stepTime = sf::seconds(1.f/60.f);

    while (window.isOpen())
    {
        sf::Time time = gameClock.restart();
        timeLastUpdate += time;
        while(timeLastUpdate > stepTime)
        {
            sf::Event event;
            while (window.pollEvent(event))
            {
                if (event.type == sf::Event::Closed)window.close();
            }
            timeLastUpdate -= stepTime;
        }
        window.clear();
       /////Drawing...
        window.display();
    }

    return 0;
}
