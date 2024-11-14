```
			LOGFONT lf;                     
			CFont* m_pFont = new CFont;
			CFont* currentFont = mainUi->GetFont();
			currentFont->GetLogFont(&lf);
			lf.lfHeight = 20;
			m_pFont->CreateFontIndirect(&lf);
			mainUi->GetDlgItem(m_uiEdit.curCH2)->SetFont(m_pFont);

```