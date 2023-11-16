#include "AssetsManager.hpp"

AssetsManager::AssetsManager()
{
    //ctor
}

AssetsManager& AssetsManager::getInstance()
{
        static AssetsManager _am;
        return _am;
}
const sf::Texture& AssetsManager::getTexture(std::string _path)
{
    std::map<std::string,sf::Texture>::iterator it = m_textures.find(_path);
    if( it == m_textures.end() )
    {
        sf::Texture tmpTexture;
        if(!tmpTexture.loadFromFile(_path))
        {
            std::cerr << "Can not load << " << _path << std::endl;
            tmpTexture.create(40,40);
        }
        m_textures.insert(it, std::make_pair(_path,tmpTexture));
        it = m_textures.find(_path);
    }

    return it->second;
}
