#ifndef BASICINGAMEELEMENT_HPP
#define BASICINGAMEELEMENT_HPP
#include <SFML/Graphics.hpp>
#include <SFML/System.hpp>

class BasicInGameElement
{
    public:
        BasicInGameElement();
        virtual ~BasicInGameElement();
        virtual void update(sf::Time _elapsedTime)=0;
        virtual void draw(sf::RenderWindow& _window)=0;

        virtual inline sf::Vector2i& getPosition();
        virtual void inline setPosition(sf::Vector2i& _newPosition);
    protected:
        sf::Vector2i m_currentPosition;
    private:
};

#endif // BASICINGAMEELEMENT_HPP
