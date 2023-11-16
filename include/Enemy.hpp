#ifndef ENEMY_HPP
#define ENEMY_HPP
#include "BasicInGameElement.hpp"
#include "AssetsManager.hpp"


class Enemy: public BasicInGameElement
{
    public:
        Enemy();
        virtual ~Enemy();
        Enemy(const Enemy& other);
        Enemy& operator=(const Enemy& other);
        virtual void update(sf::Time _elapsedTime);
        virtual void draw(sf::RenderWindow& _window);

    protected:

    private:
    sf::Sprite m_sprite;
    sf::Vector2f m_position;
};

#endif // ENEMY_HPP
