#include "Enemy.hpp"

Enemy::Enemy()
{
     m_sprite.setTexture( AssetsManager::getInstance().getTexture("./enemy.png") );
     m_position = sf::Vector2f(320,240);
     m_sprite.setPosition(m_position);
}

Enemy::~Enemy()
{
    //dtor
}

Enemy::Enemy(const Enemy& other)
{
    //copy ctor
}

Enemy& Enemy::operator=(const Enemy& rhs)
{
    if (this == &rhs) return *this; // handle self assignment
    //assignment operator
    return *this;
}
void Enemy::update(sf::Time _elapsedTime)
{
    //change posiotn of enemy logic

    m_sprite.setPosition(m_position);
}
void Enemy::draw(sf::RenderWindow& _window)
{
    _window.draw(m_sprite);
}
