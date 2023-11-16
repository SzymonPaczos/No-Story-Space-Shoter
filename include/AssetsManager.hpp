#ifndef ASSETSMANAGER_H
#define ASSETSMANAGER_H
#include <SFML/Graphics.hpp>
#include <SFML/System.hpp>
#include <iostream>
#include <string>
#include <map>

class AssetsManager
{
    private:
        AssetsManager();
        AssetsManager( const AssetsManager & _am) = delete;
    public:
        static AssetsManager & getInstance();
        void operator=(const AssetsManager &) = delete;
        const sf::Texture& getTexture(std::string _path);

        std::map<std::string, sf::Texture> m_textures;

};
#endif // ASSETSMANAGER_H
