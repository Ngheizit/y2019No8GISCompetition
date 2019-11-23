﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using ESRI.ArcGIS.ADF.BaseClasses;
using ESRI.ArcGIS.Carto;
using ESRI.ArcGIS.Controls;

namespace Test6
{
    class OpenAttributeTable : BaseCommand
    {
        private IMapControl2 m_pMapC2;
        public OpenAttributeTable(){
            base.m_caption = "打开属性表";
        }

        public override void OnCreate(object hook)
        {
            m_pMapC2 = hook as IMapControl2;
        }
        public override void OnClick()
        {
            IFeatureLayer pFeatureLayer = (m_pMapC2 as IMapControl4).CustomProperty as IFeatureLayer;
            if (pFeatureLayer != null)
                new FormAttributeTable(pFeatureLayer).Show();
            else
                System.Windows.Forms.MessageBox.Show("无法打开该图层的属性表");
        }
    }
}